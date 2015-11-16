import matplotlib.pyplot as plt
from pandas import *
comm_atnd=read_csv('/home/preethi/Desktop/edu/growth/atnd.csv')
comm_atnd.plot(kind='barh',x='States',y='Increase in Attendance (%age of Sample School)')
plt.show()
