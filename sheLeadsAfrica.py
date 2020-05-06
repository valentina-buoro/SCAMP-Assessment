# Helpful libraries to load
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read the data set 

test_data = pd.read_csv('test.csv')
test_data

train_data = pd.read_csv('traina.csv')
train_data

#explore the dataset

test_data.shape

train_data.shape

test_data.info()

train_data.info()


#check for missing values 
test_data.isnull().sum()

train_data.isnull().sum()

#After checking for missing values, fill them. the missing values here would be filled using the mean of each column

train_data['Age'] = train_data['Age'].fillna(train_data['Age'].mean())
test_data['Age'] = test_data['Age'].fillna(train_data['Age'].mean())



#check for missing values again

train_data.isnull().sum()

test_data.isnull().sum()

sns.catplot(x = 'Embarked', kind = 'count', data = train_data)

#fill the blank spaces

train_data['Embarked'] = train_data['Embarked'].fillna('S')

train_data['Cabin'] = train_data['Cabin'].fillna('Not found')
test_data['Cabin'] = test_data['Cabin'].fillna('Not found')
test_data['Fare'] = test_data['Fare'].fillna(test_data['Fare'].mean())

#check for missing values again

train_data.isnull().sum()

test_data.isnull().sum()
# carry out exploratory data analysis
# find out the percentage of people that survived

train_data.Survived.value_counts()/len(train_data)*100

# a barplot was made to show the percentage of each gender that survived
sns.barplot(x='Sex', y= 'Survived', data = train_data)


# a bar plot was made to show the class of passengers with the most survivors
sns.barplot(x='Pclass', y= 'Survived', data = train_data)
 
  
# From the exploratory data analysis carried out, it can be seen that 38.38% of passengers survived
# of which 70 percent were female and 30 percent were male.  We can also see that class one passengers that the highest number of survivors






















