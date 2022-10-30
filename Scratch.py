# From our business task, we can ask the following questions:
    # What are the differences in the travel habits between customers and non-customers?
    # How can these travel habits be turned into marketing opportunities?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.subplots()

# START OF PYCHARM SPECIFIC CODE ONLY
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)
# END OF PYCHARM SPECIFIC CODE ONLY

# Import dataset and check shape, column datatype, and missing values
df = pd.read_csv('travel_insurance.csv')
print(df.shape)
print(df.describe())
print(df.info())

# Printing the unique values
for i in df.columns:
    print(i,"Column's unique values are:",df[i].unique())




# Replace Data Types to Boolean
# df['GraduateOrNot'] = np.where(df['GraduateOrNot'] == 'Yes', True, False)
# df['EverTravelledAbroad'] = np.where(df['EverTravelledAbroad'] == 'Yes', True, False)
# df['FrequentFlyer'] = np.where(df['FrequentFlyer'] == 'Yes', True, False)
#
# df['ChronicDiseases'] = np.where(df['ChronicDiseases'] == 1, True, False)
# df['TravelInsurance'] = np.where(df['TravelInsurance'] == 1, True, False)

# df['GovernmentSec'] = np.where(df['EmploymentType'] == 'Government Sector', True, False)
# df.drop(columns='EmploymentType', inplace=True)

df = pd.get_dummies(df, drop_first=True)

# Adjusting the AnnualIncome to make readability easier
df['AnnualIncome'] = df['AnnualIncome'] / 1000

print(df.describe())
print(df.TravelInsurance.value_counts())
print(df.info())

# Check for missing values; None exist
print(df.isnull().sum())

# Correlation matrix shows areas of interest EverTravelledAbroad, AnnualIncome, FrequentFlyer
# Family Members seem to have little to no impact
df_corr = df.corr()
print(df_corr)

# Printing the proportion of flyers that have TravelInsurance
# Appears that a large number of flyers with no TravelInsurance are: Graduates or non-GovernmentSec
# Data seems to confirms the initial hypothesis that customers more likely to travel often (buying tickets from frequent
# flyer miles) and travel abroad
bool_vars = ['GraduateOrNot', 'ChronicDiseases', 'FrequentFlyer', 'EverTravelledAbroad', 'GovernmentSec']
for i in bool_vars:
    for i in bool_vars:
        x = pd.crosstab(df['TravelInsurance'], df[i])
        print(x)

# Graduate plot
grad = sns.catplot(x='GraduateOrNot', hue='TravelInsurance', kind='count', data=df)
grad.set(title='Count of Travel Insurance by Graduate Status', xlabel='Has Graduated')
# ChronicDisease plot
cd = sns.catplot(x='ChronicDiseases', hue='TravelInsurance', kind='count', data=df)
cd.set(title='Count of Travel Insurance by Chronic Disease', xlabel='Has Chronic Disease')
# FrequentFlyer plot
ff = sns.catplot(x='FrequentFlyer', hue='TravelInsurance', kind='count', data=df)
ff.set(title='Count of Travel Insurance by Frequent Flyer', xlabel='Frequent Flyer')
# EverTravelledAbroad plot
ta = sns.catplot(x='EverTravelledAbroad', hue='TravelInsurance', kind='count', data=df)
ta.set(title='Count of Travel Insurance by Travelled abroad', xlabel='Has Travelled Abroad')

# Visualizing the Age and Income data
# Appears that there is a high number of 28 year old travellers without Travel Insurance
# Appears that there is a stronger concentration of high income earners (Income > 1.2M) that purchase TravelInsurance
a = sns.catplot(x='Age', col='TravelInsurance', kind='count', data=df)
g = sns.catplot(y='AnnualIncome', x='Age', kind='box', data=df, col="TravelInsurance")
# plt.show(block=True)

# Taking a deeper look into the breakdown of travellers under 30
# High percentage of those that have travelled abroad have purchased TravelInsurance
# Those working in the GovernmentSec have the highest TravelInsurance decline rate
young = df.loc[(df['Age'] < 30)]
for i in bool_vars:
    x = pd.crosstab(young['TravelInsurance'], young[i])
    print(x)


uninsured = df[(df['TravelInsurance'] == False) & (df['GraduateOrNot'] == True)]
uninsured.drop(columns=['TravelInsurance', 'GraduateOrNot'])
print(uninsured.count())






# under_30_grads = under_30[(under_30['GraduateOrNot'] == True) & (under_30['TravelInsurance'] == False)]
# under_30.drop(columns=['GraduateOrNot', 'TravelInsurance'])
#
# print(under_30_grads[under_30_grads['AnnualIncome'] < 1000])






















# fig, ax = plt.subplots(2, 2, figsize=(16,10))
# fig.suptitle('Areas of Opportunity')
# fig = sns.countplot('EverTravelledAbroad', hue='TravelInsurance', data=df, ax=ax[0,0])
# fig = sns.countplot('FrequentFlyer', hue='TravelInsurance', data=df, ax=ax[0,1])
# fig = sns.countplot('GovernmentSec', hue='TravelInsurance', data=df, ax=ax[1,0])
# fig = sns.scatterplot(x='Age', y='AnnualIncome', hue='TravelInsurance', alpha=0.5, data=df, ax=ax[1,1])



# # Correlation matrix to see if any strong correlations exist
# # Areas of interest = EverTravelledAbroad, AnnualIncome, FrequentFlyer
# insured = df[df['TravelInsurance'] == True].drop(columns='TravelInsurance')
# uninsured = df[df['TravelInsurance'] == False].drop(columns='TravelInsurance')
# insured_corr = insured.corr()
# print(insured_corr)
# # sns.heatmap(insured_corr, annot=True)
# # plt.show()
# # uninsured_corr = uninsured.corr()
# # sns.heatmap(uninsured_corr, annot=True)
# # plt.show()
#
# ax = plt.subplots()
# sns.catplot(x='Age', kind='count', col='TravelInsurance', data=df)
# # g.set(title='Insured by Age vs. Annual Income')
# plt.show()




# Charts indicate that frequent flyers and those that travel abroad do not tend to buy insurance
# fig, ax = plt.subplots(2, 2, figsize=(16,10))
# fig.suptitle('Areas of Opportunity')
# sns.countplot('EverTravelledAbroad', hue='TravelInsurance', data=df, ax=ax[0,0])
# sns.countplot('FrequentFlyer', hue='TravelInsurance', data=df, ax=ax[0,1])
# sns.countplot('GovernmentSec', hue='TravelInsurance', data=df, ax=ax[1,0])
# sns.scatterplot(x='Age', y='AnnualIncome', hue='TravelInsurance', alpha=0.5, data=df, ax=ax[1,1])
# plt.show()

# Annual income vs Age appears to show that higher wage earners buy insurance regardless of age
# sns.countplot(x='Age', hue='TravelInsurance', data=df)
# plt.show()

# twenty_eight = df[df['Age'] == 28].drop(columns='Age')
# print(twenty_eight.corr())
# sns.countplot(x='GovernmentSec', hue='TravelInsurance', data=twenty_eight)
# plt.show()

# sns.countplot('AnnualIncome', hue='TravelInsurance', data=twenty_eight)
# plt.show()

# twenty_eight_under_30k = df[(df['Age'] == 28) & (df['AnnualIncome'] <= 1100000)].drop(columns='Age')
# print(twenty_eight_under_30k.corr())
# # sns.heatmap(twenty_eight_under_30k.corr())
# # sns.countplot(x='GraduateOrNot', hue='TravelInsurance', data=twenty_eight_under_30k)
# sns.countplot('AnnualIncome', hue='GovernmentSec', data=twenty_eight_under_30k)
# plt.show()


# fig, ax = plt.subplots(1, 2, figsize=(16,10), sharey=True)
# fig.suptitle('Customers based on Income')
# high_wage = df.loc[df['AnnualIncome'] > 1000000]
# low_wage = df.loc[df['AnnualIncome'] < 1000000]
# sns.countplot(x='Age', hue='TravelInsurance', data=high_wage, ax=ax[0])
# sns.countplot(x='Age', hue='TravelInsurance', data=low_wage, ax=ax[1])
# plt.show()


# Shows those with chronic diseases tend to decline travel insurance
# _ = sns.countplot(x='ChronicDiseases', hue='TravelInsurance', data=df)
# _.set(title='Chronic diseases with Travel Insurance')
# plt.show()



# insured = df.loc[df['TravelInsurance'] == True].drop(columns='TravelInsurance')
# _ = sns.countplot(x='Age', hue='FrequentFlyer', data=insured, palette='pastel')
# _.set(title='Insured - FrequentFlyer Count')
# plt.show()

# _ = sns.countplot('EverTravelledAbroad', hue='TravelInsurance', data=df)
# plt.show()

# _ = sns.countplot('FrequentFlyer', hue='TravelInsurance', data=df)
# plt.show()


# customers = df[(df['TravelInsurance']) == True & (df['FrequentFlyer'] == True)]
# print(customers.value_counts(normalize=True))

# Create DataFrame of FrequentFlyer's and those that have EverTravelledAbroad
# customers = df[(df.FrequentFlyer == True) & (df.EverTravelledAbroad == True)]
# print(customers.value_counts(normalize=True))
# print(customers.TravelInsurance.value_counts(normalize=True))
#
# non_customers = df[(df.FrequentFlyer == False) & (df.EverTravelledAbroad == False)]


# g = sns.barplot(x='TravelInsurance', y='AnnualIncome', hue='GovernmentSec', data=non_customers)
#
#
#
# # g = sns.barplot(x=df.FrequentFlyer, y=df.AnnualIncome, hue=df.EverTravelledAbroad)
# plt.show()


# corr = df.corr()
# g = sns.heatmap(corr, cmap='coolwarm', annot=True)
# sns.despine()
# g.figure.set_size_inches(16,10)
# plt.show()

# Grouping by FrequentFlyer's and EverTravelledAbroad
# customers = df_clean.groupby(['FrequentFlyer', 'EverTravelledAbroad'], as_index=False)
# print(customers.sum())

# import matplotlib.pyplot as plt
# import seaborn as sns
# corr = df.corr()
# g = sns.heatmap(corr, cmap='coolwarm', annot=True)
# sns.despine()
# g.figure.set_size_inches(14,10)
# plt.show()