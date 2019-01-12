""""
Build it
Train it
Test it

https://youtu.be/h3l4qz76JhQ


"""

import numpy as np

def nonlin(x, deriv=False): # sigmoid function -- кновертация входящих
    # значений в вероятности (от 0 до 1)
    if(deriv==True):
        return (x*(1-x))

    return 1/(1+np.exp(-x))

#input data
X = np.array([[0,0,1],  # Note: there is a typo on this line in the video
            [0,1,1],
            [1,0,1],
            [1,1,1]])

#output data
y = np.array([[0],
             [1],
             [1],
             [0]])

np.random.seed(1) # генерируем рандомные числа на вход

#synapses
syn0 = 2*np.random.random((3,4)) - 1  # 3x4 matrix of weights ((2 inputs + 1 bias) x 4 nodes in the hidden layer)
syn1 = 2*np.random.random((4,1)) - 1  # 4x1 matrix of weights. (4 nodes x 1 output) - no bias term in the hidden layer.

#training step
for j in range(60000): # внутри этого цикла идет обучение
    l0 = X
    l1 = nonlin(np.dot(l0, syn0)) # первое предсказание: перемножаем матрицы между каждым слоем и его синапсом,
    # вычисляем сигмоиду для всех элементов полученной матрицы
    l2 = nonlin(np.dot(l1, syn1)) # тоже самое для следующего слоя, уточненное предсказание во втором слое

    l2_error = y - l2 # сравним ожидаемый выход с реальным, вычислив ошибку при помощи вычитания

    if(j % 10000) == 0: # также посчитаем среднюю ошибку на каком-нибудь интервале, чтобы посмотреть
        # и убедиться, что с ходом обучения ошибка уменьшается
        print("Error:" + str(np.mean(np.abs(l2_error))))

    l2_delta = l2_error*nonlin(l2, deriv=True) # умножим ошибку на результат сигмоидной функции,
    # таким образом посчитаем производную выходного значения со второго слоя.
    # Эту поправку мы будем использовать, чтобы уменьшить ошибку

    l1_error = l2_delta.dot(syn1.T) # нужно понять вклад первого слоя в ошибку на втором слое
    # или Backpropagation (обратное распространение ошибки)
    # умножаем поправку со второго слоя на транспонированный синапс

    l1_delta = l1_error * nonlin(l1, deriv=True)
    # Вычислим поправку с первого слоя аналогично поправке со второго слоя
    # Умножаем ошибку с первого слоя на сигмоидную функцию
    #

    #update weights with gradient descent
    # используем вычисленные поправки для обновления весов в следующих итерациях обучения (gradient descent)
    syn1 += l1.T.dot(l2_delta)# умножаем каждый слой на поправку
    syn0 += l0.T.dot(l1_delta)

print("Output after training")
print(l2)


"""

Ошибка снижается в ходе итераций обучения

Error:0.4964100319027255
Error:0.008584525653247157
Error:0.005789459862507806
Error:0.004629176776769983
Error:0.003958765280273646
Error:0.0035101225678616736

Итоговые результаты демонстрируют У - уверенность

Output after training
[[0.00260572]
 [0.99672209]
 [0.99701711]
 [0.00386759]]
 
 """