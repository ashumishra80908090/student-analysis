import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

#Load Database
df=pd.read_csv('data.csv')
print("First five rows")
print(df.head())

#check Data
print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

#Gender Distribution
plt.figure(figsize=(6,5))
sn.countplot(data=df, x="gender")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

#Average Scores by Degree
de=df.groupby("degree").agg({"math score":'mean',"reading score":'mean',"writing score":'mean'})
print(de)
plt.figure(figsize=(13,6))
sn.heatmap(de,annot=True,cmap="coolwarm")
plt.title("Student score based on degree")
plt.show()


#Frome the chart represent average score based on test course
te=df.groupby("test course").agg({"math score":'mean',"reading score":'mean',"writing score":'mean'})
print(te)
plt.figure(figsize=(10,5))
sn.heatmap(te,annot=True, cmap="viridis")
plt.title("Student score based on test")
plt.show()

plt.figure(figsize=(10,5))
sn.boxplot(data=df,x="math score")
plt.title("Math score")
plt.show()

plt.figure(figsize=(10,5))
sn.boxplot(data=df,x="reading score")
plt.title("Reading score")
plt.show()

plt.figure(figsize=(10,5))
sn.boxplot(data=df,x="writing score")
plt.title("Writing score")
plt.show()

#Distribution of groups
print(df["groups"].unique())
groupA=df.loc[(df['groups']=="group A")].count()
groupB=df.loc[(df['groups']=="group B")].count()
groupC=df.loc[(df['groups']=="group C")].count()
groupD=df.loc[(df['groups']=="group D")].count()
groupE=df.loc[(df['groups']=="group E")].count()

l=["Group A","Group B","Group C","Group D","Group E"]
lis=[groupA["groups"], groupB["groups"], groupC["groups"], groupD["groups"], groupE["groups"]]
myexplodes=[0,0,0.1,0,0]
plt.pie(lis,labels=l,autopct="%1.2f%%",explode=myexplodes)
plt.title("Distribution of groups")
plt.show()
