
# # Cuantitative data analysis grafic

# import numpy as np

# import pandas as pd

# import matplotlib.pyplot as plt

# from scipy.optimize import curve_fit

# from scipy.stats import pearsonr  # Importa pearsonr

# # Leer datos de un archivo Excel
# # Por Nombre de Columna
# datos = pd.read_excel('pruebes_physics.xlsx', header=1, usecols=['x', 'y'])

# # # Por Índice de Columna
# # datos = pd.read_excel('pruebes_physics.xlsx', header=1, usecols=[1, 2])

# # # Por Rango de Columnas (usando letras de columna de Excel)
# # datos = pd.read_excel('pruebes_physics.xlsx', header=1, usecols='B:C')

# print(datos)
# print(datos.columns)

# # Independient variable
# z1 = datos["x"]

# # Dependient variable
# z2 = datos["y"]

# # Fuction curve ajust
# def func(s,a,b):
# 	return a*s + b

# params, params_covariance = curve_fit(func, z1, z2)

# a_fit, b_fit = params	

# z1_smooth = np.linspace(min(z1), max(z1), 100)
# z2_smooth = func(z1_smooth, a_fit, b_fit)

# plt.plot(z1, z2, 'r-', label='Original curve')
# plt.plot(z1_smooth, z2_smooth, 'b--', label='fitting curve')

# plt.xlabel('H')
# plt.ylabel('cH')

# plt.scatter(z1,z2, label='Data', color='black')
# plt.legend()
# print(a_fit, b_fit)

# # Calcular el coeficiente de correlación de Pearson
# coeficiente_pearson, p_valor = pearsonr(z1, z2)

# # Calculate the position for the label to be above the center
# x_label = (min(z1) + max(z1)) / 2
# y_label = (min(z2) + max(z2)) / 1.7

# # Adjustment function of the fitting curve
# if round(b_fit, 5) == 0:
# 	adjustment_function = "y = {:.5f}x".format(a_fit)
# elif b_fit < 0:
# 	adjustment_function = "y = {:.5f}x - {:.5f}".format(a_fit, abs(b_fit))
# else:
# 	adjustment_function = "y = {:.5f}x + {:.5f}".format(a_fit, abs(b_fit))


# # Title
# plt.title('cH vs H')



# # Pearson Coeficient

# plt.text(x_label, (y_label*1.7/1.8), f"Pearson Coeficient: {round(coeficiente_pearson, 4)}", ha='center', va='center', color='blue')


# # Place a label above the center
# plt.text(x_label, y_label, adjustment_function, ha='right', va='center', color='blue')

# # Cuadricule
# plt.grid(True)


# plt.show()

# print(f"Coeficiente de Pearson: {coeficiente_pearson}")
# print(f"P-valor: {p_valor}")









# Cualitative data analysis grafic

import matplotlib.pyplot as plt
import pandas as pd

# Supongamos que 'datos' es tu DataFrame con los datos que deseas graficar
datos = pd.read_excel('pruebes_physics.xlsx', header=1, usecols=['x', 'y'])

# Crear una figura y un eje
fig, ax = plt.subplots()

# Graficar los datos
ax.plot(datos['x'], datos['y'], label='Curva original')

# Eliminar las etiquetas de los ejes
# ax.set_xticklabels([])
# ax.set_yticklabels([])
plt.xlabel('T')
plt.ylabel('X')
plt.title('Distance variation with time')


# Eliminar los valores numéricos de los ejes
ax.set_xticks([])
ax.set_yticks([])

# Opcional: eliminar la leyenda si no deseas mostrarla
ax.legend().remove()

# Mostrar la gráfica
plt.show()
