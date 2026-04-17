# import numpy as np
# import pandas as pd
# from collections import Counter
# from sklearn.model_selection import train_test_split

# def manhattan_distance(x1, x2):
#   distance = np.sum(np.abs(x1 - x2))
#   return distance

# class KNN:
#   def __init__(self, k):
#     self.k = k

#   def fit(self, X, y):
#     self.X_train = X
#     self.y_train = y

#   def predict(self, X):
#     predictions = [self._predict(x) for x in X]
#     return predictions

#   def _predict(self, x):
#     distances = [manhattan_distance(x, x_train) for x_train in self.X_train]
#     k_indices = np.argsort(distances)[:self.k]
#     k_nearest_labels = [self.y_train[i] for i in k_indices]
#     most_common = Counter(k_nearest_labels).most_common()
#     return most_common[0][0]

# df = pd.read_csv('fruits.csv')
# y = df['fruit_label'].values
# X = df[['mass','width','height','color_score']].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

# clf = KNN(k=5)
# clf.fit(X_train, y_train)
# predictions = clf.predict(X_test)

# print("Predictions:",predictions)
# accuracy = np.sum(predictions == y_test) / len(y_test)
# print("Accuracy:", accuracy)


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
fruit_df = pd.read_csv('fruit.csv')

# Features and target
X = fruit_df[['mass', 'width', 'height', 'color_score']]
y = fruit_df['fruit_label']   # same idea as 'Type' in glass

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Distance metrics
distance_metrics = [
    ('Euclidean', 'minkowski'),
    ('Manhattan', 'manhattan')
]

# Loop (same structure)
for name, metric in distance_metrics:
    knn = KNeighborsClassifier(n_neighbors=3, metric=metric)

    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    # SAME label handling as glass
    all_labels = np.unique(y)

    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred, labels=all_labels)

    print(f"\n--- KNN with {name} Distance ---")
    print(f"Accuracy: {acc:.4f}")
    print("Confusion Matrix:")
    print(cm)
