import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv("Customer Churn.csv")

#Exploring Data
print(data.describe())  
print(data.info())
print(data.shape)

#Check For Missing Value and Duplicates
print(data.isnull().sum())
print(data.duplicated())

#Data Cleaning
data['TotalCharges']= data["TotalCharges"].replace(" ","0")
data['TotalCharges']= data["TotalCharges"].astype(float)
data['customerID'].duplicated().sum()

#Conversion Of Data
def conv(value):
    if value == 1:
        return "yes"
    else:
        return "no"
    
data["SeniorCitizen"] = data["SeniorCitizen"].apply(conv)
print(data["SeniorCitizen"].head(10))

#Churn Analysis
Churn = data["Churn"].value_counts()

#Count Plot For Churn
ax = sns.countplot(x = "Churn",data=data)
ax.bar_label(ax.containers[0])
plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

#Pie Chart For Churn
plt.pie(Churn,autopct="%1.2f%%",labels=Churn.index)
plt.title("Percentage Of Churned Customer")
plt.show()

#Churned Customer By Gender
ax =sns.countplot(x="gender",data= data,hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Gender")
plt.ylabel("No Of Customer Churned By Gender")
plt.show()

#Churned Customer By Senior Citizens
churn_seniorcitizens = data.groupby(['gender', 'Churn']).size().unstack()
churn_seniorcitizens.plot(kind='bar', stacked=True, figsize=(8, 5))
plt.title("Churn Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.legend(title="Churn")
plt.tight_layout()
plt.show()

#Churned Customer By Tenure
plt.figure(figsize=(9,4))
sns.histplot(x="tenure",data=data,bins = 72,hue="Churn")
plt.title("Customer Churned By Tenure")
plt.xlabel("Months")
plt.ylabel("No Of Customers")
plt.show()

#Churned On Basis Of Contract
ax = sns.countplot(x="Contract",data=data,hue ="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.ylabel("No Of Customers")
plt.show()

#Churned Analysis By Subploting For Other Services Offered To Customers
columns = [
    "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
    "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies"
]

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(20, 15), constrained_layout=True)
axes = axes.flatten()
for i, col in enumerate(columns):
    sns.countplot(data=data, x=col, ax=axes[i], order=data[col].value_counts().index,hue="Churn")
    axes[i].set_title(col, fontsize=14)
    axes[i].tick_params(axis='x')
fig.suptitle('Count Plots of Service Features', fontsize=20, y=1.03)
plt.show()

#Churned Customers By Payment Method
plt.figure(figsize=(6,4))
ax = sns.countplot(x="PaymentMethod",data=data,hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Customer Churned By Payment Method")
plt.xticks(rotation = 45)
plt.show()
