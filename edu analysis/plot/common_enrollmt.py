import matplotlib.pyplot as plt
from pandas import *
common_enroll=read_csv('/home/preethi/Desktop/edu/growth/enroll.csv')
common_enroll.plot(kind='barh',x='States',y='Increase in Enrolment (%age of Sample School)')
plt.show()
