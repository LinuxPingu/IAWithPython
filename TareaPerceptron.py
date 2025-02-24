from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
import random

# Data de entrenamiento
#X = [[random.randint(1,9),random.randint(1,9)] for _ in range(8)];
# Data default 
X = [[2,3],[1,1],[4,2],[3,6],[5,7],[6,1],[7,5],[8,2]];
print(X)
y = [1,0,1,1,1,0,0,0];

# Utilizando la librería sklearn, podemos crea de manera rápida un perceptrón con casi la misma información vista en clase.
# Para crear nuestro percentron, se requieren de 2 variables
#   1) max_iter : La cantidad de iteraciones que nuestro perceptron va a recorer, es el equivalente a las epocas 
#   2) eta0: es el learning rate establecido
# 
# Dato extra: La funcion de Perceptron, de manera default, establece los pesos de manera aleatorea de forma similar al ejemplo visto en clase, de ser necesario establecer algun tipo de peso lo podemos definir con la variable random_state 
perceptron = Perceptron(max_iter=100,eta0=0.1);

# Parte de las facilidades que presenta la libreria, podemos utilizar la funcion fit para comenzar a entrenar nuestro modelo
# A diferencia de lo visto en clase, la funcion fit no utiliza heavyside para entrenar su modelo, utiliza decision linear
# Ver presentacion para las diferencias 
perceptron.fit(X,y);

# De esta forma, podemos extraer los valores de los pesos y los bias para poder graficar nuestros resultados
weights = perceptron.coef_[0]
bias = perceptron.intercept_[0]


# Settemos los valores para dibujar la línea de decisión
# Para los planos 2D, utilizamos la formula vista en clase w1*x1 + w2*x2 + b = 0 --> x2 = -(w1/w2)*x1 - (b/w2)
x_values = np.linspace(0, 10, 100)
decision_boundary = -(weights[0] / weights[1]) * x_values - (bias / weights[1])

# Clasificamos los puntos con respecto al array y y X siendo 1 los azules y 0 los rojos
for i, label in enumerate(y):
    if label == 1:
        plt.scatter(X[i][0], X[i][1], color="blue")
    else:
        plt.scatter(X[i][0], X[i][1], color="red")

# Setteamos la línea de decisión
plt.plot(x_values, decision_boundary, color="green", label="Resultado")

plt.xlabel("Objetos X")
plt.ylabel("Objetos Y")
plt.title("Perceptron")
plt.grid(True)
plt.show()