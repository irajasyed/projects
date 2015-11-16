import matplotlib.pyplot as plt
from pandas import *
y_axs='Number of Students'

students=read_csv('/home/preethi/Desktop/edu/Tamilnadu/tn_corp.csv')
students['Number of Students'].plot()
plt.xlabel("No of Schools")
plt.ylabel("No of Students")

plt.show()
students[['Community - Backward community','Community - Most Backward community','Community - Other Castes']].plot()
plt.show()
