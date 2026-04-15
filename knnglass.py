import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

glass_df = pd.read_csv('glass.csv')
X = glass_df.drop('Type', axis=1)
y = glass_df['Type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

distance_metrics = [
  ('Euclidean', 'minkowski'),
  ('Manhattan', 'manhattan')
]


for name, metric in distance_metrics:
  knn = KNeighborsClassifier(n_neighbors=3, metric=metric)

  knn.fit(X_train, y_train)
  y_pred = knn.predict(X_test)

  all_labels = np.unique(y)
  acc = accuracy_score(y_test, y_pred)
  cm = confusion_matrix(y_test, y_pred, labels=all_labels)

  print(f"\n--- KNN with {name} Distance ---")
  print(f"Accuracy: {acc:.4f}")
  print("Confusion Matrix:")
  print(cm)