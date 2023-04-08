import numpy as np
import matplotlib.pyplot as plt

barWidth=0.20
fig=plt.subplots(figsize=(10,5))

BTech=[18,15.5,15]
MTech=[13.02,13,12]
MS=[15,11.94,14]
MBA=[15.35,11.50,14.25]

br1=np.arange(len(BTech))
br2=[x+barWidth for x in br1]
br3=[x+barWidth for x in br2]
br4=[x+barWidth for x in br3]

plt.bar(br1,BTech,color='r',width=barWidth,edgecolor='black',label='BTech')
plt.bar(br2,MTech,color='b',width=barWidth,edgecolor='black',label='MTech')
plt.bar(br3,MS,color='g',width=barWidth,edgecolor='black',label='MS')
plt.bar(br4,MBA,color='y',width=barWidth,edgecolor='black',label='MBA')


plt.xlabel("Year")
plt.ylabel("Packages offered")
plt.xticks([r+barWidth for r in range(len(BTech))],['2022','2021','2020'])
plt.title("Placements at IITM")
plt.legend()
plt.show()
