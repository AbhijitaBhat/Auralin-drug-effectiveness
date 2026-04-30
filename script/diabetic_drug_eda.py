import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
patients = pd.read_csv("data/patients_cl.csv")
treatment = pd.read_csv("data/treatment_ultra_cleaned.csv")
patients.head()
treatment.head()
patients.info()
treatment.info()
#Calculate percentage change of HbA1C
percent_change_HbA1C = treatment['hba1c_pct_change'] = (treatment['hba1c_start'] - treatment['hba1c_end']) / treatment['hba1c_start'] * 100
treatment[['hba1c_start', 'hba1c_end', 'hba1c_change', 'hba1c_pct_change']].head()
patients['patient_id'].duplicated().sum()
treatment['patient_id'].duplicated().sum()
patients['patient_id'].duplicated().sum()
treatment['patient_id'].duplicated().sum()
percent_change_HbA1C.describe()
#Check for missing values
treatment.isnull().sum()
patients.describe()
data = pd.merge(treatment, patients, on='patient_id', how="inner")
#Dropping the unnecessary columns
columns_to_drop = ['given_name_x', 'surname_x', 'given_name_y', 'surname_y',
                   'address', 'city', 'state', 'zip_code', 'country',
                   'email', 'Phone_no']
data.drop(columns=columns_to_drop, inplace=True, errors='ignore')
print(data.isnull().sum())
#HbA1C change
data['hba1c_change'] = data['hba1c_start'] - data['hba1c_end']
#BMI Calculation
data = data[data['height'] > 0]
data['BMI'] = data['weight'] / ((data['height'] / 100) ** 2)
data.describe()
#Age Calculation
from datetime import datetime
data['birthdate'] = pd.to_datetime(data['birthdate'], errors='coerce')
today = pd.to_datetime('1-25-2026')
data['age'] = (today - data['birthdate']).dt.days // 365
#Histogram of BMI
plt.figure(figsize=(8,5))
sns.histplot(data['BMI'], bins=20, kde=True, color='lightgreen')
plt.title('Distribution of BMI')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
#Scatterplot of BMI VS HbA1C levels
plt.figure(figsize=(8,5))
sns.scatterplot(x='BMI', y='hba1c_change', data=data, hue='medicine_type', palette='coolwarm')
plt.title('Relationship Between BMI and HbA1c Change')
plt.xlabel('BMI')
plt.ylabel('HbA1c Change')
plt.tight_layout()
plt.show()
#Boxplot: HbA1C by medicine type
plt.figure(figsize=(8,5))
sns.boxplot(x='medicine_type', y='hba1c_change', data=data, palette='Set2')
plt.title('HbA1c Change by Medicine Type')
plt.xlabel('Medicine Type')
plt.ylabel('HbA1c Change')
plt.tight_layout()
plt.show()
#Histogram of Age
plt.figure(figsize=(8,5))
sns.histplot(data['age'], bins=20, kde=True, color='orange')
plt.title('Distribution of Age')
plt.xlabel('Age (years)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
#Sctterplot Age VS HbA1C change
plt.figure(figsize=(8,5))
sns.scatterplot(x='age', y='hba1c_change', data=data, hue='medicine_type', palette='coolwarm')
plt.title('Relationship Between Age and HbA1c Change')
plt.xlabel('Age (years)')
plt.ylabel('HbA1c Change')
plt.tight_layout()
plt.show()
#Boxplot: HbA1C change by age group
bins = [0, 30, 45, 60, 75, 100]
labels = ['<30', '30-45', '45-60', '60-75', '75+']
data['age_group'] = pd.cut(data['age'], bins=bins, labels=labels)
plt.figure(figsize=(8,5))
sns.boxplot(x='age_group', y='hba1c_change', data=data, palette='Set3')
plt.title('HbA1c Change by Age Group')
plt.xlabel('Age Group')
plt.ylabel('HbA1c Change')
plt.tight_layout()
plt.show()
























