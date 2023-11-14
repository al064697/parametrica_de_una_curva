import matplotlib.pyplot as plt
import numpy as np

# Definir la función vectorial r(t)
def r(t):
    x = 1 + t**2
    y = np.cos(t)**2
    return x, y


# Crear valores de t
t_values = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Obtener las coordenadas x, y para cada valor de t
x_values, y_values = r(t_values)

# Graficar la función vectorial
plt.plot(x_values, y_values, label=r'$\mathbf{r}(t) = \langle 1 + t^2, \cos^2(t) \rangle$')

# Etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de la función vectorial')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
