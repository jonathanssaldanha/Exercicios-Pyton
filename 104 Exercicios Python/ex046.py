#   FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE
#   FOGOS DE ARTIFICIO, INDO DE 10 ATE 0, COM UMA PAUSE DE 1 SEGUNDO ENTRE ELAS.

from time import sleep
for cont in range(20, -1, -1):
    print(cont)
    sleep(0.1)
print('BUM BUM BUM')