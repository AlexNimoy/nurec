import yaml         # для работы с YAML
import os           # для работы с операционной системой
import Levenshtein  # для вычисления расстояния Левенштейна между строками

class Nurec:
    """
    Класс Nurec используется для сравнения распознанных данных c изображений
    в формате JSON с тестовыми данными, хранящимися в YAML.
    При создании экземпляра класса в него передаются распознанные JSON данные,
    затем вызывается метод load_yaml_and_compare для загрузки соответствующих
    YAML и сравнения значений. Класс также предоставляет методы
    для вычисления точности сравнения, получения деталей несовпадений
    и общего количества различающихся символов.
    """
    def __init__(self, recognized_data):
        """
        Конструктор класса Nurec.
        Инициализирует экземпляр класса с распознанными JSON данными.
        recognized_data - данные изображения в формате JSON
        """
        self.recognized_data = recognized_data  # создаем JSON объект с данными
        self.total_chars = 0                    # присваиваем 0 общему количеству символов
        self.mismatched_chars = 0               # присваиваем 0 количеству ошибок
        self.details_list = []                  # создаем пустой список несовпадений
        self.load_yaml_and_compare()            # добавляем метод сравнения

    def load_yaml_and_compare(self):
        """
        Метод сравнения данных JSON и YAML
        """
        for data in self.recognized_data:                                            # Обход данных JSON
            file_name = data["File Name"]                                            # Получение имени JSON файла
            module_dir = os.path.dirname(os.path.abspath(__file__))                  # Выбор директории с этим кодом
            yaml_file_path = os.path.join(module_dir, 'images', f"{file_name}.yaml") # Сохранение пути к YAML

            with open(yaml_file_path, 'r') as f:  # Открытие данных YAML
                yaml_data = yaml.safe_load(f)     # Загрузка данных YAML

            for key, value in data.items():                         # перебор ключа и значения в словаре JSON
                if key in yaml_data:                                # если ключ есть в YAML
                    if isinstance(value, list):                     # если значение является списком
                        for i, item in enumerate(value):            # обходим каждый элемент списка
                            for sub_key, sub_value in item.items(): # перебор ключа и значения внутри элемента списка
                                if sub_key in yaml_data[key][i]:    # если ключ есть в YAML вызывается метод сравнения
                                    self.compare_values(sub_value, yaml_data[key][i][sub_key], file_name, sub_key)
                    else:                                           # если значение не список вызывается метод сравнения сразу
                        self.compare_values(value, yaml_data[key], file_name, key)

    def compare_values(self, recognized_value, yaml_value, file_name, key_name):
        """
        Метод для сравнения значений и обновления атрибутов
        recognized_value - распознанные JSON данные, имеющиеся в YAML
        yaml_value - данные YAML файла
        key_name - совпадающий ключ JSON и YAML
        """
        self.total_chars += max(len(recognized_value), len(yaml_value))     # Увеличивает общее количество символов на максимум JSON или YAML
        mismatched = False                                                  # Устанавливаем флаг "отсутствие ошибок" по умолчанию
        lev_distance = Levenshtein.distance(recognized_value, yaml_value)   # Вычисление расстояния Левенштейна (количество вставок, удалений или замен, чтобы JSON==YAML)
        self.mismatched_chars += lev_distance                               # Увеличиваем ошибку на количество ошибок Левенштейна

        if lev_distance > 0:  # Если расстояние Левенштейна больше 0
            mismatched = True # устанавливаем флаг "ошибоки есть"

        if mismatched:        # Если флаг "ошибки есть" информацию (имя файла, ключ, левеншстейна, значения JSON и YAML) добавляем в список
            self.details_list.append({
                "file_name": file_name,
                "key_name": key_name,
                "distance": lev_distance,
                "expected": yaml_value,
                "received": recognized_value
            })

    def accuracy(self):
        """
        Метод класса для вычисления точности по итогам сравнения JSON и YAML
        """
        if self.total_chars == 0:                                     # Предотвращаем деление на 0
            return 0
        return 100 - (self.mismatched_chars / self.total_chars * 100) # При наличие совпадений JSON и YAML, возвращаем % ошибки

    def details(self):
        """
        Метод для получения результирующей строки списка деталей сравнения
        """
        result_str = ""                  # создаем пустую строку
        for detail in self.details_list: # пробегаем по списку деталей и добавляем их в результат
            result_str += f"[{detail['key_name']}] {detail['file_name']}\n"
            result_str += f"distance: {detail['distance']}\n"
            result_str += f"expected:\n{detail['expected']}\n"
            result_str += f"received:\n{detail['received']}\n\n"
        return result_str.rstrip()

    def total_distance(self):
        """
        Метод для получения общего количества различающихся символов
        """
        return self.mismatched_chars

    def get_verification_images(self):
        """
        Метод для возвращения списка путей до изображений ".png" в выбранной дирректории
        """
        verification_images = []
        path_to_images = r'Путь до папки с изображениями'

        for filename in os.listdir(path_to_images):
            if filename.endswith(".png"):
                verification_images.append(os.path.join(path_to_images, filename))

        return verification_images

    def save_to_file(self, file_path):
        """
        Метод создания текстового файла содержащего список путей до изображений ".png"
        """
        verification_images_list = self.get_verification_images()
        with open(file_path, 'w') as file:
            for image_path in verification_images_list:
                file.write(image_path + '\n')
