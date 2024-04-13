"""
* The machine learning program: This program Machine lean from csv file.
* Teruaki Murakami
* 2023/12/06

1. Read data (csv file).
2. Make data label
3. Prepossessing data.
4. Make train data and test data.
5. Build model
6. Compile model
7. Train data
8. Test data (show loss)
9. Test Ai model by input number
10. Save model
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data from CSV file
data = pd.read_csv('BTC_NEG_IVE_AI7.csv')

# Extract features (X) and labels (y)
X = data[["number"]]
y = data['flag']

# Get feature names
feature_names = X.columns

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=feature_names)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled_df, y, test_size=0.2, random_state=42)

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(1)
])

#Compile the model with Adam optimizer and mean squared error loss
model.compile(optimizer='adam', loss='mean_squared_error')

#Train the model on the training data
model.fit(X_train, y_train, epochs=1200, batch_size=1, validation_data=(X_test, y_test))

#Evaluate the model on the test data
loss = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}')

# Continuous input loop for obtaining new data and making predictions
while True:
    # Initialize list for input values
    input_list = [0]

    # Accept user input (in this case, just one input)
    for i in range(1):
        input_list[i] = input(str(i) + ":")

        # Check for termination signal ("999") to save the model and exit
        if input_list[i] == "999":
            model.save('tensorflow/asset', save_format='tf')
            break

    #Exit loop if termination signal is received
    if input_list[0] == "999":
        break

    #Convert input list to a numpy array and scale using the trained scaler
    new_data = np.array([input_list])
    new_data_scaled = scaler.transform(new_data)

    #Make a prediction using the trained model
    prediction = model.predict(new_data_scaled)
    print(f'Predicted Flag for the new data: {prediction[0][0]}')
