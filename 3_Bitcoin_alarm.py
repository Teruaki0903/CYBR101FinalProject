"""
* The bitcoin alarm program: Use ai model, use Ritetag API, send warning mail, Make time schedule.
* Teruaki Murakami
* 2023/12/6

1. Input how many times check the tweets.
2. Check next time.
3. Use (time.sleep ) method.
4. Call hashtag function:
4-1. Call Ritetag API: client.hashtag_stats(['bitcoin'])
4-2. get Number of tweets about bitcoin per one hour.
4-3. Call Ai function:
4-3-1. Read data label from csv file.
4-3-2. Preprocessing.
4-3-3. Load saved model.
4-3-4. Input Number of tweets per one hour.
4-3-4. Check current situation is safe or not.
4-4 (if situation is safe). Just print number of tweets.
4-4 (if situation is not safe). Call mail function.
4-4-1. Dispatch Outlook mail
4-4-2. Create mail item.
4-4-3. Set mail setting (make title, body message (input number of tweets) , send email address)
4-4-4. Send message.
5. Go back to 3.

"""

import win32com.client
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import time
from ritetag import RiteTagApi  # Assuming this is a custom module for RiteTag API

#Define a function for handling hashtags and sending alerts
def hashtag():
    access_token = 'd66581c61b216f8eaa4c21f18a671cbf039bed2d1615'
    client = RiteTagApi(access_token)

    def limit_80_percentage_reached(limit):
        message = 'Used {}% of API credits. The limit resets on {}'.format(limit.usage, limit.reset)
        print(message)

    client.on_limit(80, limit_80_percentage_reached)

    #Retrieve hashtag statistics for 'bitcoin'
    stats = client.hashtag_stats(['bitcoin'])

    for data in stats:
        print('#{}: {} tweets per hour'.format(data.hashtag, data.tweets))
        if 50 < AI(data.tweets):
            print("Warning!\n check the position.")
            mail(data.tweets)

#Define a function for making predictions using saved model
def AI(number):
    # Load data from a CSV file
    data = pd.read_csv('BTC_NEG_IVE_AI.csv')

    # Extract and standardize features
    X = data[['number']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Load a pre-trained TensorFlow model
    loaded_model = tf.keras.models.load_model('tensorflow/asset')

    # Input new data for prediction
    new_data = np.array([[number]])
    new_data_scaled = scaler.transform(new_data)
    prediction = loaded_model.predict(new_data_scaled)

    return prediction[0][0]

# Define a function for sending email alerts
def mail(number):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.to = "kitamuras@lopers.unk.edu"
    mail.subject = "Bitcoin alarm"
    mail.bodyFormat = 1
    mail.body = "Bitcoin alarm was issued\nThe number of tweets: " + str(number)
    mail.display(False)
    mail.Send()

# Introduction message
intro = "This is a bitcoin alarm. Please input the check time."

# Initialize variables for check times
count = []
wait_flag = False

# User input for the number of checks per day
print(intro)
number_of_checks_oneday = int(input("The time (per one day):"))

#Calculate the check time interval
check_time = int(24 / number_of_checks_oneday)

#Populate the array with check times
for i in range(number_of_checks_oneday + 1):
    count.append(round(check_time * i))

print("The time when we will check: " + str(count))

#Get current time in hours and minutes
unix_time = time.time()
current_time = time.localtime(unix_time)
formatted_time_hour = int(time.strftime('%H', current_time))
formatted_time_minutes = int(time.strftime('%M', current_time))

#Debug: Print minutes and hours
#print(str(60 - formatted_time_minutes))
#print(str(formatted_time_hour))

#Mail debug
#mail(1000)

hashtag()

# Check if the next check is within 60 minutes
for i in count:
    if formatted_time_hour + 1 == i:
        wait_flag = True

# Perform the next check (if the next check is within 60 minutes)
if wait_flag:
    time.sleep((60 - formatted_time_minutes) * 60)
    # print("check")  # Debugging print # Keep as is for non-critical times; comment out for critical times
    hashtag()  # Call the API function # Keep as is for non-critical times; uncomment for critical times

# Regular time checks
while True:
    for i in count:
        if formatted_time_hour + 1 == i:
            wait_flag = True

    time.sleep(3600)
    # print("check")  # Debugging print # Keep as is for non-critical times; comment out for critical times
    hashtag()  # Call the API function # Keep as is for non-critical times; uncomment for critical times

