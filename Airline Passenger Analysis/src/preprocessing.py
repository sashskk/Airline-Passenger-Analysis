import pandas as pd

def age_category(age):
    if age < 25:
        return 'Young'
    elif age <= 60:
        return 'Medium'
    else:
        return 'Old'


# Preprocessing
data = pd.read_csv('../data/train.csv')

rows, columns = data.shape
print(f'Count of rows: {rows}')
print(f'Count of columns: {columns}')

print(data.dtypes)

print(data.describe())

print(data.columns.tolist())
print(data.head(10))

print(data.isna().sum())

data['Arrival Delay in Minutes'] = data['Arrival Delay in Minutes'].fillna(0)
data = data.drop('Unnamed: 0', axis = 1)

# Replacing categorical data types
obj_data = data.select_dtypes(include=['object']).copy(deep=True)
print(obj_data)

gender = {'Female': 0, 'Male': 1}
data['Gender'] = data['Gender'].map(gender)

customer_t = {'Loyal Customer': 0, 'disloyal Customer': 1}
data['Customer Type'] = data['Customer Type'].map(customer_t)

travel_t = {'Business travel': 0, 'Personal Travel': 1}
data['Type of Travel'] = data['Type of Travel'].map(travel_t)

t_class = {'Business': 0, 'Eco': 1, 'Eco Plus': 2}
data['Class'] = data['Class'].map(t_class)

satisf_t = {'neutral or dissatisfied': 0, 'satisfied': 1}
data['satisfaction'] = data['satisfaction'].map(satisf_t)


# Analysis

# General statistics

df_satis_dur = data.groupby('satisfaction')['id'].sum()
df_total = df_satis_dur.sum()
shares_by_satis = round(((df_satis_dur / df_total) * 100), 2)
shares_by_satis = shares_by_satis.reset_index()
shares_by_satis.columns = ['Satisfaction', 'Percentage']
print(shares_by_satis)

average_age = data['Age'].mean().round(2)
print(f'Average age is {average_age} years')

df_loyal_dis = data['Customer Type'].value_counts()
share_loys_vs_dis = round(((df_loyal_dis / df_loyal_dis.sum()) * 100), 2)
print(share_loys_vs_dis)

# Factors of satisfaction

service_columns = [
    'Inflight wifi service',
    'Departure/Arrival time convenient',
    'Ease of Online booking',
    'Gate location',
    'Food and drink',
    'Online boarding',
    'Seat comfort',
    'Inflight entertainment',
    'On-board service',
    'Leg room service',
    'Baggage handling',
    'Checkin service',
    'Inflight service',
    'Cleanliness'
]

df_mean_scores = data.groupby('satisfaction')[service_columns].mean().round(2).T
df_mean_scores.columns = ['dissatisfied', 'satisfied']
df_mean_scores['diff'] = df_mean_scores['satisfied'] - df_mean_scores['dissatisfied']
df_mean_scores = df_mean_scores.sort_values(by='satisfied', ascending=False)
print(df_mean_scores)

print(df_mean_scores['satisfied'].head(4))

class_service_means = data.groupby('Class')[service_columns].mean().round(2).T
print(class_service_means)

# Segmentation of passengers

man_vs_women = data.groupby(['Gender', 'satisfaction']).size().unstack()
man_vs_women_pct = round(((man_vs_women / man_vs_women.sum()) * 100), 2)
print(man_vs_women_pct)

loyalty_satisfaction = data.groupby(['Customer Type', 'satisfaction']).size().unstack()
loyalty_satisfaction_pct = round(((loyalty_satisfaction / loyalty_satisfaction.sum()) * 100), 2)
print(loyalty_satisfaction_pct)
loyalty_services = data.groupby('Customer Type')[service_columns].mean().round(2)
print(loyalty_services)

age_allocation = data['Age'].apply(age_category)
age_allocation = age_allocation.value_counts()
age_allocation_pct = round(((age_allocation / age_allocation.sum()) * 100), 2)
print(age_allocation_pct)

data['AgeGroup'] = data['Age'].apply(age_category)
age_satisfaction = data.groupby('AgeGroup')['satisfaction'].count()
age_satisfaction = age_satisfaction.reset_index()
age_satisfaction.columns = ['Age group', 'Count']
print(age_satisfaction)

