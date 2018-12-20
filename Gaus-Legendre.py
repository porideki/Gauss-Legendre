import math
xw = [{"x":[0], "w":[2]},
    {"x": [-math.sqrt(1 / 3), math.sqrt(1 / 3)], "w": [1, 1]},
    {"x": [-math.sqrt(3 / 5), 0, math.sqrt(3 / 5)], "w": [5 / 9, 8 / 9, 5 / 9]},
    {"x":[-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116], "w":[-0.3478548451, -0.6521451549, 0.6521451549, 0.3478548451]}]

def gauslegendre(bottom, top, n):
    area = 0
    for i in range(0, n):
        area += xw[n - 1]["w"][i] * g(bottom, top, xw[n - 1]["x"][i])

    area *= 0.5 * (top - bottom)
    
    return area

def g(bottom, top, t):
    return f(0.5 * (top - bottom) * t + 0.5 * (top + bottom))

def f(x):
    #ここを変更
    return (math.e ** x) * (math.sin(x) ** 2)

if __name__ == "__main__":
    print("I =", gauslegendre(0, 1, 3))