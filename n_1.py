# Дана функция f(x) = -12x^4-18x^3+5x^2+10x-30
import math
from sympy import *
from sympy.plotting import plot

# 1 Определить корни
x = Symbol('x')
func=-12*x**4-18*x**3+5*x**2+10*x-30
y=solve(func)
x1=float(y[0])
x2=float(y[1])
x3=float(y[2])
x4=float(y[3])
print(x1, x2, x3, x4)

# 2 Найти интервалы, на которых функция возрастает
fd=diff(func)
print(solve(0<fd))

# 3 Найти интервалы, на которых функция убывает
print(solve(fd<0))

# 4 Построить график
plot(func, (x, -250, 250))

# 5 Вычислить вершину
print(solve(fd)[0])

# 6 Определить промежутки, на котором f > 0
solve(func>0)

# 7 Определить промежутки, на котором f < 0
solve(func<0)