import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.utils import shuffle

diabetes = pd.read_csv("OriginalDataset.csv")

diabetes = shuffle(diabetes,random_state = 22)

diabetes = pd.DataFrame(diabetes).fillna(method='ffill')

from sklearn.preprocessing import LabelEncoder

# Convert target label to numerical Data
le = LabelEncoder()
diabetes['diabetes status'] = le.fit_transform(diabetes['diabetes status'])
#diabetes['occupation'] = le.fit_transform(diabetes['occupation'])

from sklearn.model_selection import train_test_split
X = diabetes.drop(columns=['diabetes status','occupation'])
y = diabetes['diabetes status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

# Creating Random Forest Model
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20)
classifier.fit(X_train, y_train)

classifier.fit(X_test,y_test)

# Import GridSearchCV
from sklearn.model_selection import GridSearchCV

# Optimize model paramaters

#Set your parameter grid here
param_grid = {}
grid_model = GridSearchCV(classifier, param_grid)
grid_model.fit(X_train, y_train)
grid_model.fit(X_test,y_test)
print(grid_model.best_params_)

# import evaluation metrics
from sklearn.metrics import confusion_matrix, accuracy_score

#evaluate the model
y_pred = classifier.predict(X_test)

# Get error rate
print("Error rate of Random Forest classifier: ", 1 - accuracy_score(y_test, y_pred))

# Get confusion matrix
confusion_matrix(y_pred, y_test)

accuracy = accuracy_score(y_pred, y_test) * 100
print('Accuracy: %f' % accuracy)

# Creating a pickle file for the classifier
filename = 'diabetes-prediction-rfc-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))