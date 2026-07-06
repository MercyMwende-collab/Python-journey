import pandas as pd

df = pd.read_csv('supermarket_sales.csv')


df['Date'] = pd.to_datetime(df['Date'])#convert Date column to datetime format
print(df['Date'].dtype)#check data type of Date column
print(df['Date'].head())#check first 5 rows of Date column

print(df.duplicated().sum())#check for duplicate rows in the dataset

print(df[['cogs','Tax 5%','Sales']].head())#check first 5 rows of cogs, Tax 5% and Sales columns

sales_by_branch = df.groupby('Branch')['Sales'].sum()#group by Branch and sum the Sales column
print(sales_by_branch)#print the total sales by branch

sales_by_product = df.groupby('Product line')['Sales'].sum().sort_values(ascending=False)
print(sales_by_product)#group by Product line and sum the Sales column, then sort in descending order

sales_by_payment = df.groupby('Payment')['Sales'].sum().sort_values(ascending=False)
print(sales_by_payment)#group by Payment and sum the Sales column, then sort in descending order    

df['Month'] = df['Date'].dt.month#extract month from Date column and create a new column Month
sales_by_month = df.groupby('Month')['Sales'].sum()#group by Month and sum the Sales column
print(sales_by_month)#print the total sales by month    

print(df['Time'].head())#check first 5 rows of Time column

df['Hour'] = pd.to_datetime(df['Time'], format='%I:%M:%S %p').dt.hour
sales_by_hour = df.groupby('Hour')['Sales'].sum().sort_values(ascending=False)
print(sales_by_hour)

pivot = df.pivot_table(values='Sales', index='Branch', columns='Product line', aggfunc='sum')
print(pivot)
