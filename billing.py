import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
l_below_date=[]
l_below_balance=[]
daily=[]
daily_balance=[]
def get_sales_input():
    a=list(map(int,input("enter the sales in months seprated by space entered value will be calculated in crores").split()))
    l=len(a)
    return a,l
bank_balance = 10000000.00 
df=pd.read_csv("bills.csv")
df['Date']=pd.to_datetime(df["Date"],format='%m%d%Y)
df['rem']=pd.to_datetime(df["rem"])
df["by days"]=pd.to_numeric(df["by days"])
df["Amount"]=pd.to_numeric(df["Amount"])
df['rem']=df["rem"]+pd.Timedelta(days=90)
df.dropna(inplace = True)
date_start=pd.to_datetime("31-Dec-2022")
d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
i=int(input("enter the year going on"))
pay_day=df["rem"]
start=0
if i%4==0 and i%100!=0:
    d[2]=29
sales,no_of_months=get_sales_input()
for i in range(no_of_months):
    sales[i]=(sales[i]*10000000)/d[i+1]
for i in range(no_of_months):
    for j in range(d[i+1]):
        date_start=date_start+pd.Timedelta(days=1)
        bank_balance=bank_balance+sales[i]
        if date_start==pay_day[start]:
            while True:
                if date_start==pay_day[start]:
                    bank_balance-=df["Amount"][start]
                    start+=1
                    if bank_balance<0:
                        l_below_date.append(date_start)
                        l_below_balance.append(bank_balance)
                else:
                    break
        daily.append(date_start)    
        daily_balance.append(bank_balance)
df2 = pd.DataFrame(list(zip(l_below_balance, l_below_date)), columns =['balance left', 'on the date'])
df_left=pd.DataFrame(list(zip(daily,daily_balance)),columns=["date","bank balance"])
df_left.to_csv("daily_balance.csv")
df2.to_csv("negativebalance.csv")