# ===============================================
# Titanic EDA – Steps 1 to 5
# ===============================================

# Step 1: Import Libraries & Load Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  # better visuals

# Load Titanic dataset (adjust path if needed)
df = pd.read_csv("titanic.csv")  # or full path if not in same folder

# Step 1: Preview data
print("===== Dataset Preview =====")
print(df.head())
print("\nShape of dataset:", df.shape)
print("\nColumns in dataset:", df.columns)

# Step 2: Dataset Info & Summary
print("\n===== Dataset Info =====")
df.info()

print("\n===== Statistical Summary =====")
print(df.describe())

print("\n===== Missing Values =====")
print(df.isnull().sum())

# Step 3: Univariate Analysis

# Numerical Variables
# Age
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=df['Age'])
plt.title("Age Boxplot")
plt.show()

# Fare
plt.figure(figsize=(6,4))
sns.histplot(df['Fare'], bins=30, kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=df['Fare'])
plt.title("Fare Boxplot")
plt.show()

# Categorical Variables
# Survived
plt.figure(figsize=(5,4))
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

# Sex
plt.figure(figsize=(5,4))
sns.countplot(x='Sex', data=df)
plt.title("Gender Count")
plt.show()

# Pclass
plt.figure(figsize=(5,4))
sns.countplot(x='Pclass', data=df)
plt.title("Passenger Class Count")
plt.show()

# Embarked
plt.figure(figsize=(5,4))
sns.countplot(x='Embarked', data=df)
plt.title("Port of Embarkation Count")
plt.show()

# Step 4: Bivariate Analysis

# Survival vs Gender
plt.figure(figsize=(6,4))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival Count by Gender")
plt.show()

# Survival vs Pclass
plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival Count by Passenger Class")
plt.show()

# Age vs Survival
plt.figure(figsize=(6,4))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age Distribution by Survival")
plt.show()

# Fare vs Survival
plt.figure(figsize=(6,4))
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title("Fare Distribution by Survival")
plt.show()

# Embarked vs Survival
plt.figure(figsize=(6,4))
sns.countplot(x='Embarked', hue='Survived', data=df)
plt.title("Survival by Port of Embarkation")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Step 5: Multivariate Analysis – Pairplot
sns.pairplot(df[['Survived','Age','Fare','Pclass']])
plt.show()
