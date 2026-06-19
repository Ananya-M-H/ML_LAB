import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("https://raw.githubusercontent.com/gchoi/Dataset/master/ToyotaCorolla.csv")
print(data.head())
# a) Scatter Plot
plt.figure()
plt.scatter(data['KM'], data['Doors'])
plt.title("Scatter Plot: KM vs Doors")
plt.xlabel("KM")
plt.ylabel("Doors")
plt.show()

# b) Box Plot
plt.boxplot([data["Price"], data["HP"], data["KM"]])
plt.title("Box Plot: Price, HP, KM")
plt.show()

# c) Heatmap - Seaborn
sns.heatmap(data[["Price", "KM", "Doors", "Weight"]].corr())
plt.title("Heatmap of Correlations")
plt.show()

# d) Contour Plot
plt.tricontourf(data['KM'], data['Weight'], data['Price'])
plt.title("Contour Plot: KM vs Weight with Price")
plt.show()

# e) 3D Surface Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(data['KM'], data['Doors'], data['Price'])
ax.set_title("3D Surface Plot: KM, Doors, Price")
plt.show()