import matplotlib.pyplot as plot
import numpy as np


def calculate_linear_regression(x, y):
    n = len(x)
    m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
    c = (np.sum(y) - m * np.sum(x)) / n

    print("Linear Regression Equation: y = mx + c")
    print(f"Slope (m): {m}")
    print(f"Intercept (c): {c}")
    print(f"Equation of the line: y = {m:.2f}x + {c:.2f}")
    return m, c


def r_squared_value(y_actual, y_predicted):
    n = len(x)
    mean = np.mean(y_actual)
    result = (1- np.sum(y_actual - y_predicted)**2 / np.sum(y_actual - mean)**2)
    print("R Squared Value: ", result)
    return result

# x = np.array([1.12345123, -1.23456789, 0.56473829, -0.84329741, -1.84756234,
#               0.29485738, -0.65749321, 1.84567943, -1.02948573, 0.73458921,
#               0.52934857, -1.39485738, 1.39485738, -0.84756234, 0.98234567,
#               -1.14573829, 0.84329741, 1.02948573, -0.45673829, 0.65749321])

# y = np.array([-1.39485738, 1.02948573, 0.84329741, -0.45673829, -1.14573829,
#               0.98234567, -1.39485738, 0.73458921, -0.84329741, 0.65749321,
#               0.56473829, -1.02948573, 1.39485738, -0.65749321, 1.84567943,
#               -1.84756234, 0.52934857, 0.29485738, -1.23456789, 1.12345123])

x = np.random.randn(20) 
y = np.random.randn(20)  

print("x:", x)
print("y:", y)

m, c = calculate_linear_regression(x, y)

plot.scatter(x, y, color="red", label="Data Points")


y_line = m * x + c
plot.plot(x, y_line, color="blue", label="Regression Line")


x_new = 21
y_new = m * x_new + c
print(f"Forecasted y-value for x = {x_new}: {y_new:.2f}")
plot.scatter(x_new, y_new, color="green", label=f"Forecasted Point ({x_new}, {y_new:.2f})", zorder=5)

r_squared = r_squared_value(y, y_line)

plot.xlabel("x - axis")
plot.ylabel("y - axis")
plot.title("Random Scatter Plot of 20 Pts")
plot.legend()

plot.show()
