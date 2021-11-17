# Library Import
import matplotlib.pyplot as plt
import numpy as np


# Dataset (from Ansys)
dt = np.array([
         [18 , 0.22148609],
         [65 , 0.22131121],
         [80 , 0.21917301],
         [100 , 0.21686321],
         [120 , 0.21484317],
         [140 , 0.21353279],
         [145 , 0.21320634],
         [160 , 0.21223401],
         [200 , 0.21028894],
         [210 , 0.20984355],
         [220 , 0.20945567],
])

# Establishing the X and Y datum 
velocity = dt[:, 0]
dragcoefficient = dt[:, 1]


# Calculating parameter
theta = np.polyfit(velocity, dragcoefficient, 1)
print(f'The parameters of the line: {theta}')

# Now, calculating the y-axis values against x-values according to
# the parameters
y_line = theta[1] + theta[0] * velocity


correlation_matrix = np.corrcoef(velocity, dragcoefficient)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print(f'The parameters of the line: {theta}')


# Plotting the data points and the best fit line
plt.scatter(velocity, dragcoefficient)
plt.plot(velocity, y_line, 'r')
plt.title('Vehicle Velocity vs. Drag Coefficient')
plt.ylabel('Drag Coefficient')
plt.xlabel('Velocity [km/h]')
plt.grid(True)

plt.show()
