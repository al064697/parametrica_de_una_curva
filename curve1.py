import matplotlib.pyplot as plt
import numpy as np

# Definir la función paramétrica
def parametric_function(t):
    x = t**2 - 2*t
    y = t + 1
    return x, y

# Crear valores de t
t_values = np.linspace(-5, 5, 100)  # Puedes ajustar el rango según sea necesario

# Obtener las coordenadas x, y para cada valor de t
x_values, y_values = parametric_function(t_values)

# Graficar la curva paramétrica
plt.plot(x_values, y_values, label='Curva paramétrica: $\\{ t^2 - 2t, t + 1 \\}$')
plt.scatter(x_values, y_values, color='red')  # Marcar puntos

# Etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de la Curva Paramétrica')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
