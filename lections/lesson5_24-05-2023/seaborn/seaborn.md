# Отображение статистики

# Отображение статистических отношений

```python
import seaborn as sns
```

### отображение точек долготы по отношению к широте

```python
sns.scatterplot(data=df, x='longitude', y='latitude')
```

### отношение, чем выше количество семей, тем выше количество людей и соответственно комнат

```python
sns.scatterplot(data=df, x="households", y="population", hue="total_rooms")
```

### отношение, чем выше количество семей, тем выше количество людей и соответственно комнат / размер = 10

```python
sns.scatterplot(data=df, x="households", y="population", hue="total_rooms", size=10)
```

### сразу несколько вызуализаций через встроенный метод PairGrid

```python
cols = ['population', 'median_income', 'housing_median_age',
'median_house_value']
g = sns.PairGrid(df[cols])
g.map(sns.scatterplot)
```

# Линейные графики

### metod relplot для визуализации выбирается тип line:

```python
sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)
```

### metod relplot для визуализации выбирается тип line:

```python
sns.relplot(x="longitude", y="median_house_value", kind="line", data=df)
```

- Используя точечный график можно визуализировать эти отношения с большей четкостью. Скорее всего резкий рост цен связан с близостью к ценному объекту,
  повышающему качество жизни, скорее всего побережью океана или реки.

```python
sns.scatterplot(data=df, x="latitude", y="longitude", hue="median_house_value")
```

## Гистограмма

Способ представления табличных данных в графическом виде — в виде столбчатой
диаграммы. По оси x обычно указывают значение, а по оси y - встречаемость(кол-во
таких значений в выборке)

```python
sns.histplot(data=df, x="median_income")
```

Можно видеть что у большинства семей доход находится между значениями 2 и 6. И
только очень небольшое количество людей обладают доходом > 10.
Изобразим гистограмму по housing_median_age.

```python
sns.histplot(data = df, x = 'housing_median_age')
```

Распределение по возрасту более равномерное. Большую часть жителей
составляют люди в возрасте от 20 до 40 лет. Но и молодежи не мало. Также очень
много пожилых людей > 50 лет медианный возраст.
Давайте посмотрим медианный доход у пожилых жителей.

```python
sns.histplot(data=df[df['housing_median_age']>50], x="median_income")
```

Давайте разобьем возрастные группы на 3 категории те кто моложе 20 лет, от 20 до
50 и от 50, чтобы посмотреть влияет ли это на доход.

```python
df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50),
'age_group'] = 'Ср. возраст'
df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'
```

Что в этом случае происходит внутри таблицы? Добавился новый столбец
age_group, в котором будет указана соответствующая категория.

Применим group_by, чтобы получить среднее значение.

```python
df.groupby('age_group')['median_income'].mean().plot(kind='bar')
```

Молодые оказываются самой богатой группой населения. Но отличие в доходе не
значительное.

**Seaborn** так же позволяет нам смотреть распределение по многим параметрам.
Давайте поделим группы по доходам на 2. Те у кого медианный доход выше 6 и те у
кого меньше. Изобразим дополнительное измерение с помощью оттенка в виде
возрастных групп и групп по доходам.

```python
df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'
sns.displot(df, x="median_house_value", hue="income_group")
```
