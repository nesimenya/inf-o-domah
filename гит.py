import pandas as pd
import matplotlib.pyplot as plt
table= pd.read_csv(r'C:\Users\n.molodkin\Downloads\zillow.csv')
sort=table.sort_values(by='ListPrice')
table= pd.DataFrame(sort)
grf= table.groupby('Beds').ListPrice.min()
grf.plot.bar(x='Beds',y='ListPrice',rot=0,color='g')
plt.show()
