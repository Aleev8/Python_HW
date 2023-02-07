# Урок 11. Jupyter Notebook и несколько слов об аналитике
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 1.Определить корни
# 2.Найти интервалы, на которых функция возрастает
# 3.Найти интервалы, на которых функция убывает
# 4.Построить график
# 5.Вычислить вершину
# 6.Определить промежутки, на котором f > 0
# 7.Определить промежутки, на котором f < 0

import sympy
import matplotlib.pyplot as plt
import numpy as np
from sympy import solveset
from sympy import sin, cos, pi



x = sympy.symbols('x')
f = -12*(x**4)*sin(cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
roots = solveset(f)
print(roots)

x = np.arange(-5, 5, 0.01)

f = f = -12*(x**4)*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30

plt.plot(x, f)
plt.grid(color='g')