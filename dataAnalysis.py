"""
Created on Tue Sep 12 22:15:58 2023

@author: ahbmt
"""
import numpy as np
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import statistics as stat
plt.rcParams['figure.dpi'] = 300

# Dados
users = [1,2,3,4,5,6,7,8,9,10,11]
times = [60,62,75,122,65,67,110,64,88,93,72] # em segundos
ages = [22,25,28,52,21,22,61,28,34,42,19] # em anos

# Média
avg = stat.mean(times)
avgList = []
for x in users:
  avgList.append(avg)
# Mediana
median = stat.median(times)
medianList = []
for x in users:
  medianList.append(median)
# Desvio padrão
stdev = stat.stdev(times)
stdevList = []
for x in users:
  stdevList.append(stdev)

# Classificação dos dados de tempo em faixas
under60List = []
under60Age = []

bet60to80List = []
bet60to80Age = []

over80List = []
over80Age = []

for x in range(len(users)):
  if times[x] <= 60:
     under60List.append(users[x])
     under60Age.append(ages[x])
  elif times[x] <= 80:
     bet60to80List.append(users[x])
     bet60to80Age.append(ages[x])
  else:
     over80List.append(users[x])
     over80Age.append(ages[x])

# Plot Tempo x Usuários
plt.figure(1)
plt.plot(users, times,'or',label='Dado bruto')
plt.plot(users, avgList,'--g',label='Média')
plt.plot(users, medianList,'--b',label='Mediana')
plt.ylabel('Tempo de execução da tarefa (s)')
plt.xlabel('Número de identificação dos usuários')
plt.legend()
plt.show()

# Plot Idade x Tempo ordenados - Regressão linear
timesArray = np.array(times).reshape((-1, 1))
agesArray = np.array(ages).reshape((-1, 1))
model = LinearRegression().fit(agesArray, timesArray)

plt.figure(2)
plt.plot(ages, times,'or',label='Dados')
plt.plot(ages,model.predict(agesArray),'k',label='Regressão linear')
plt.plot(ages, avgList,'--g',label='Média')
plt.plot(ages, medianList,'--b',label='Mediana')
plt.ylabel('Tempo de execução da tarefa (s)')
plt.xlabel('Idade dos usuários (Anos)')
plt.legend()
plt.show()

# Pizza plot
plt.figure(3)
labels = 'Menos de 60s', 'Entre 60 e 80s', 'Acima de 80s'
sizes = [len(under60List), len(bet60to80List), len(over80List)]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')