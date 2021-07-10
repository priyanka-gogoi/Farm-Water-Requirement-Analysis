import pandas as pd
from datetime import datetime, date
from sklearn.model_selection import StratifiedShuffleSplit


def predict_wr(forminput):
  dataset = pd.read_csv('Water_requirement_train_data.csv')
  dataset['date'] = pd.to_datetime(dataset['date'], format = '%d-%m-%Y')
  dataset['year'] = dataset['date'].dt.year
  dataset['month'] = dataset['date'].dt.month
  dataset['day'] = dataset['date'].dt.day
  first_column = dataset.pop('year')
  second_column = dataset.pop('month')
  third_column = dataset.pop('day')
  dataset.insert(1, 'year', first_column)
  dataset.insert(2, 'month', second_column)
  dataset.insert(3, 'day', third_column)

  split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
  for train_index, test_index in split.split(dataset, dataset['Kc']):
    strat_train_set = dataset.loc[train_index]

  dataset= strat_train_set.copy()

  X = dataset.iloc[:, 2:11].values
  y = dataset.iloc[:, -1].values

  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

  from sklearn.linear_model import LinearRegression
  regressor = LinearRegression()

  regressor.fit(X_train, y_train)

  y_pred = regressor.predict(forminput)

  return y_pred