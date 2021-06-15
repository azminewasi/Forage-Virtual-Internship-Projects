import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
data_file = 'data.csv'
df = pd.read_csv (data_file)
df=df[df["txn_description"]=="PAY/SALARY"]

df.drop(['customer_id','transaction_id','long_lat','merchant_code','currency','movement','extraction','bpay_biller_code','country','merchant_long_lat','status','card_present_flag','merchant_suburb','merchant_state','date','txn_description','first_name','merchant_id'],axis='columns', inplace=True)


corr=df.corr().round(2)
print("Correlation Matrix:")
print(corr)

X2=df[['age','balance']]
Y=df['amount']
X_tr,X_ts,Y_tr,Y_ts=train_test_split(X2,Y,test_size=0.3,random_state=1)
model=LinearRegression()
model.fit(X_tr,Y_tr)
Y_predicted=model.predict(X_ts)

print("\n\nMean Squared Error>> ",mean_squared_error(Y_ts,Y_predicted).round(2))
print("Model Score >>", model.score(X_ts,Y_ts),"\n\n")

