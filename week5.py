import pandas as pd
from sklearn.preprocessing import StandardScaler

titanic_data = pd.read_csv('titanic_dataset.csv')
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)

titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)

titanic_data.drop(columns=['Cabin'], inplace=True)

titanic_data.dropna(inplace=True)

titanic_data['Title'] = titanic_data['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

titanic_data['Title'] = titanic_data['Title'].replace(['Lady', 'Countess','Capt', 'Col',
                                                      'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
titanic_data['Title'] = titanic_data['Title'].replace('Mlle', 'Miss')
titanic_data['Title'] = titanic_data['Title'].replace('Ms', 'Miss')
titanic_data['Title'] = titanic_data['Title'].replace('Mme', 'Mrs')

# Drop the 'Name' column
titanic_data.drop(columns=['Name'], inplace=True)

# One-hot encode 'Sex'
titanic_data = pd.get_dummies(titanic_data, columns=['Sex'], drop_first=True)

# One-hot encode 'Embarked'
titanic_data = pd.get_dummies(titanic_data, columns=['Embarked'], drop_first=True)

# One-hot encode 'Title'
titanic_data = pd.get_dummies(titanic_data, columns=['Title'], drop_first=True)

# Initialize the scaler
scaler = StandardScaler()

# List of numerical features to scale
numerical_features = ['Age', 'Fare']

# Scale the numerical features
titanic_data[numerical_features] = scaler.fit_transform(titanic_data[numerical_features])

# Display the preprocessed dataset
print(titanic_data.head())
