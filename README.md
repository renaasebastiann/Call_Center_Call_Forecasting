# Call_Center_Call_Forecasting
# Call Center Forecasting Project

## Overview

This project develops a forecasting model to predict the number of calls received by a call center each day over the next two weeks based on historical data collected from January 1, 2021, to March 31, 2021. The project leverages SARIMA

## Libraries Used

The project requires the following Python libraries:

- NumPy
- pandas
- statsmodels
- scikit-learn
- mysql-connector-python


### Prerequisites

Before running the executable, ensure you have the following installed:

- Python 3.x
- MySQL Server

### Install Required Libraries

To install the required Python libraries, use pip:

pip install numpy pandas statsmodels scikit-learn mysql-connector-python

##Database Configuration

MySQL Setup:

-Ensure you have MySQL Server running.
-Create a database (e.g., call_center_db) to store the call data.

##Database Connection:

-Modify the database connection settings in the script (Final_Project.py) if necessary. 
-Update the following parameters:
host: Your MySQL server address (e.g., localhost)
user: Your MySQL username
password: Your MySQL password
database: The name of the database you created (e.g., call_center_db)

##Sample Connection Code
-python
-Copy code

import mysql.connector
db_connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='call_center_db'
)
