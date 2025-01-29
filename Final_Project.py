


import numpy as np
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

def load_data_from_mysql():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql123',
        database='call_center'
    )

    query = """
    SELECT call_id, agent, call_date, call_time, topic, answered, resolved, 
           speed_of_answer_sec, avg_talk_duration_sec, satisfaction_rating
    FROM call_data;
    """
    data = pd.read_sql(query, connection)
    connection.close()
    return data

data = load_data_from_mysql()

data['call_date'] = pd.to_datetime(data['call_date'])
data['date'] = data['call_date'].dt.date

total_calls = data.groupby('call_date').size().reset_index(name='total_calls')


train = total_calls[:-2]
test = total_calls[-2:]
test1=total_calls[-14:]

sarima_model = SARIMAX(
    train['total_calls'],
    order=(2, 3, 3),                
    seasonal_order=(1, 1, 1, 7),   
    enforce_stationarity=False,
    enforce_invertibility=False
)
sarima_result = sarima_model.fit()

forecast = sarima_result.forecast(steps=14)

forecast_dates = pd.date_range(start=test['call_date'].max() + pd.Timedelta(days=1), periods=14)
forecast_df = pd.DataFrame({
    'call_date': forecast_dates,
    'forecasted_calls': np.round(forecast)
})

test = test.set_index('call_date')
forecast_df = forecast_df.set_index('call_date')

print("Test dates:\n", test.index)
print("Forecast dates:\n", forecast_df.index)

mae = mean_absolute_error(test1['total_calls'], forecast_df['forecasted_calls'])
print(f'SARIMA : Mean Absolute Error: {mae}')

plt.figure(figsize=(12, 6))
plt.plot(train['call_date'], train['total_calls'], label='Training Data', marker='o')
plt.plot(test.index, test['total_calls'], label='Test Data', marker='o', color='orange')
plt.plot(forecast_df.index, forecast_df['forecasted_calls'], label='Forecasted Data', marker='o', color='green')

plt.xlabel('Date')
plt.ylabel('Total Calls')
plt.title('SARIMA Forecast for Call Center Data')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
print(forecast_df)


# In[3]:


plt.figure(figsize=(12, 6))
plt.bar(train['call_date'], train['total_calls'], label='Training Data', alpha=0.6)
plt.bar(test.index, test['total_calls'], label='Test Data', alpha=0.6, color='orange')
plt.bar(forecast_df.index, forecast_df['forecasted_calls'], label='Forecasted Data', alpha=0.6, color='green')
plt.xlabel('Date')
plt.ylabel('Total Calls')
plt.title('Total Calls Forecast for Call Center Data')
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# In[4]:

train_calls = train['total_calls'].values.flatten()  
test_calls = test['total_calls'].values.flatten()    
forecast_calls = forecast_df['forecasted_calls'].values.flatten() 
plt.figure(figsize=(12, 6))
plt.fill_between(train['call_date'], train_calls, label='Training Data', alpha=0.4)
plt.fill_between(test.index, test_calls, label='Test Data', alpha=0.4, color='orange')
plt.fill_between(forecast_df.index, forecast_calls, label='Forecasted Data', alpha=0.4, color='green')
plt.xlabel('Date')
plt.ylabel('Total Calls')
plt.title('Total Calls Forecast for Call Center Data')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()


# In[5]:


plt.figure(figsize=(12, 6))
plt.scatter(train['call_date'], train['total_calls'], label='Training Data', marker='o')
plt.scatter(test.index, test['total_calls'], label='Test Data', marker='o', color='orange')
plt.scatter(forecast_df.index, forecast_df['forecasted_calls'], label='Forecasted Data', marker='o', color='green')
plt.xlabel('Date')
plt.ylabel('Total Calls')
plt.title('Total Calls Forecast for Call Center Data')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

