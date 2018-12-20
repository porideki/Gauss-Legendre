import math
xw = [{"x":[0], "w":[2]},
    {"x": [-3**(-0.5), 3**(-0.5)], "w": [1, 1]},
    {"x": [-(3 / 5)** 0.5, 0, (3 / 5)** 0.5], "w": [5 / 9, 8 / 9, 5 / 9]},
    {"x":[-8611363116, -0.3399810436, 0.3399810436, -8611363116], "w":[-0.3478548451, -0.6521451549, 0.6521451549, 0.3478548451]}]

def gauslegendre(bottom, top, n):
    area = 0
    for i in range(n):
        area += xw[n]["w"][i] * g(bottom, top, xw[n]["x"][i])
    
    return area

def g(top, bottom, t):
    return f(0.5 * (top - bottom) * t + 0.5 * (top + bottom))

def f(x):
    return (math.e ** x) * (math.sin(x) ** 2)