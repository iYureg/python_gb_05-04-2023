# **Знакомство с Google Colab**

```python
import pandas as pd
```

### читаем

```python
df = pd.read_csv('/content/sample_data/california_housing_train.csv')
```

### ряды сверху ( по умолчанию 5 )

```python
df.head(n=10)
```

### ряды снизу ( по умолчанию 5 )

```python
df.tail(n=2)
```

### количество рядов и столбцов

```python
df.shape
```

### все пустые ячейки true/false

```python
df.isnull()
```

### суммы пустых ячеек в столбцах

```python
df.isnull().sum()
```

### типы данных

```python
df.dtypes
```

### список с названиями столбцов

```python
df.columns
```

### вывод столбца 'latitude'

```python
df['latitude']
```

### вывод нескольких столбцов

```python
df[['latitude', 'population']]
```

### выборка рядов по условию

```python
df[df['housing_median_age'] < 20]
```

### выборка рядов по условию / вывод одного столбца

```python
df[df['housing_median_age'] < 20]['total_rooms']
```

### выборка рядов по условию / оператор & выполнение всех условий / вывод нескольких столбцов

```python
df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)][['total_rooms','housing_median_age']]
```

### оператор | выбиполняет первое условые которое True
