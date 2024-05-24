import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("final_data.csv")
y = data['class']
X = data.drop('class', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)
from sklearn.ensemble import RandomForestClassifier

# Create an instance of RandomForestClassifier
clf = RandomForestClassifier()

# Fit the classifier to your training data
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
# Now you can use the classifier for prediction or other operations


# model= RandomForestClassifier(n_estimators = 50, criterion = 'entropy', random_state = 0)
# model = DecisionTreeRegressor(random_state = )
# model.fit(X, y)
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(random_state = 0)
# from sklearn.svm import SVC
# model= SVC(kernel = 'linear', random_state = 0)
# model.fit(X_train, y_train)

# model.fit(X_train, y_train)
# from sklearn.neighbors import KNeighborsClassifier
# model = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
# model.fit(X_train, y_train)
# from sklearn.naive_bayes import GaussianNB
# model= GaussianNB()
# model.fit(X_train, y_train)

# pred = model.predict(X_test)
accuracy = accuracy_score(y_test, clf)

print("accuracy: " + str(accuracy * 100) + "%")

#pickle.dump(classifier, open('model.pickle', 'wb'))
with open("clf.pickle", "wb") as f:
    pickle.dump(clf, f)
# import pickle
#from sklearn.tree import DecisionTreeClassifier

# # Assume model is your trained DecisionTreeClassifier model
# # Train your model
#model = DecisionTreeClassifier()
# # Fit your model with training data

# # Save the model to a file
# with open("model.pickle", "wb") as f:
#     pickle.dump(model, f)
