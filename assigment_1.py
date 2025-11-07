import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('student_scores.csv')
x = df[['Hours']].values
y = df[['Scores']].values

theta_0 = 0 #b
theta_1 = 0 #w
alpha = 0.001 #learning rate
num_iterations = 100 #the loop will change the b & w and slightly reduce the error
mse_values = [] #Takes the difference between the real value and the predicted value → y^-y and stores it in the array


for i in range(num_iterations):
    y_pred = theta_0 + theta_1 * x## wx+b ==0 , 
    error = y - y_pred##5 ==>

    d_theta_0 = (-2 / len(x)) * np.sum(error) #how much each parameter should change to reduce error.
    d_theta_1 = (-2 / len(x)) * np.sum(error * x)

    theta_0 -= alpha * d_theta_0 #This is the gradient descent update rule.
    theta_1 -= alpha * d_theta_1

   
    mse = np.mean(error ** 2)

    mse_values.append(mse) 

print(f"MSE = {mse:.4f}")#final Mean Squared Error``