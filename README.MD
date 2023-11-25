# Test System (Neural university recognition check)

## Colab Examples

[Colab Examples](https://colab.research.google.com/drive/19878-C6WMm1ApNNEw5-Y3Xt-Tskwrgwb?usp=sharing).

## Usage

```bash
!pip install git+https://github.com/AlexNimoy/nurec.git

from nurec import Nurec
```

```python
recognized_data = [{<JSON_PARAMS>}, {...}]

result = Nurec(recognized_data)
```

### Methods

#### accuracy

`result.accuracy()`

returns accuracy like `100.00` or worse

#### details

`result.details()`

```bash
[key] file
distance: Number
expected:
String
received:
String
```

#### total_distance

returns total Levenshtein distance

`result.total_distance()`

Number

## JSON example

```json
{
  "File Name": "",
  "01 Receipt Number": "",
  "02 Receipt Date": "",
  "04 Counterparty": [
    {
      "04-01 Name": "",
      "04-02 BIN": ""
    }
  ],
  "05 Contract": "",
  "06 Our Company BIN": "",
  "07 Counterparty Bank": [
    {
      "07-01 Bank BIC": "",
      "07-02 Current Account IIC": ""
    }
  ],
  "09 Counterparty Payment Purpose Code": "",
  "10 Items Table": [
    {
      "10-01 Item": "",
      "10-02 Unit": "",
      "10-03 Quantity": "",
      "10-04 Price": "",
      "10-05 Amount": ""
    }
  ]
}
```

## Params Table

[Params Table (Google Disc)](https://docs.google.com/spreadsheets/d/14AIRNzPu7_TQo_VaDG64RQo2k1brj8DDg_k--Eqtkzk/edit#gid=0)

| №    | Описание                           | Название поля                        |
| ---- | ---------------------------------- | ------------------------------------ |
| 1    | Номер Счета                        | 01 Receipt Number                    |
| 2    | Дата Счета                         | 02 Receipt Date                      |
| 4    | Контрагент                         | 04 Counterparty                      |
| 4.1  | Наименование Контрагента           | 04-01 Name                           |
| 4.2  | БИН Контрагента                    | 04-02 BIN                            |
| 5    | Договор                            | 05 Contract                          |
| 6    | БИН Нашей организации              | 06 Our Company BIN                   |
| 7    | Банк Контрагента                   | 07 Counterparty Bank                 |
| 7.1  | БИК банка Контрагента              | 07-01 Bank BIC                       |
| 7.2  | Расчетный счет (ИИК) Контрагента   | 07-02 Current Account IIC            |
| 9    | Код назначения платежа Контрагента | 09 Counterparty Payment Purpose Code |
| 10   | Информация из табличной части:     | 10 Items Table                       |
| 10.1 | Наименование товара                | 10-01 Item                           |
| 10.2 | Единица измерения                  | 10-02 Unit                           |
| 10.3 | Количество                         | 10-03 Quantity                       |
| 10.4 | Цена                               | 10-04 Price                          |
| 10.5 | Сумма                              | 10-05 Amount                         |

## Как отправить pull request (Contribute)

Please follow [CONTRIBUTING.md](CONTRIBUTING.md).
