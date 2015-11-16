import matplotlib.pyplot as plt
from pandas import *
y_axs='With Pucca building'
common_enroll=read_csv('/home/preethi/Desktop/edu/Infra/inf.csv')
common_enroll.plot(kind='barh',x='States\UT',y=y_axs)
plt.show()
