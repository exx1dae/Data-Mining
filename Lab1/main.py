import pandas as pd

data = pd.read_csv('./data/train.csv', index_col='PassengerId')

filteredPassengers = data[(data['Embarked'] == 'C') & (data.Fare > 200)].head()

# Определить сколько женщин/мужчин было на борту

countOfWomen = data[data['Sex'] == 'female'].shape[0] # 314
countOfMen = data[data['Sex'] == 'male'].shape[0] # 577

# Вывести распределение переменной Pclass (социально-экономический статус) и это же распределение только для мужчин/женщин по отдельности. Сколько было мужчин 2-го класса?

# Распределение переменной Pclass
pclass_distribution = data['Pclass'].value_counts()
print(pclass_distribution)

# Распределение для мужчин
male_pclass_distribution = data[data['Sex'] == 'male']['Pclass'].value_counts()

# Распределение для женщин
female_pclass_distribution = data[data['Sex'] == 'female']['Pclass'].value_counts()

print("Male Pclass distribution:")
print(male_pclass_distribution)

print("\nFemale Pclass distribution:")
print(female_pclass_distribution)

# Количество мужчин 2-го класса
male_count_2nd_class = male_pclass_distribution.get(2, 0)
print("Number of males in 2nd class:", male_count_2nd_class)

