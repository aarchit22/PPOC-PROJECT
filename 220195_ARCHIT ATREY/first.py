import numpy as np
import matplotlib.pyplot as plt

data={'A':2,'B':3,'C':4}
features=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(10,5))
plt.bar('A',2,color='r',width=0.4)
plt.bar('B',3,color='b',width=0.4)
plt.bar('C',4,color='g',width=0.4)
plt.xlabel("Features")
plt.ylabel("Values")
plt.title("Assignment graph")
plt.show()
