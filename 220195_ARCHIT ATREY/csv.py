import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\Users\91840\Music\World_Press_Index_2021.csv')

best_2019 = df.loc[df['Global Score 2019'].idxmin()]
worst_2021 = df.loc[df['Global Score 2021'].idxmax()]

plt.bar(['Best Global Score 2019', 'Worst Global Score 2021'], [best_2019['Global Score 2019'], worst_2021['Global Score 2021']])
plt.show()