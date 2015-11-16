import matplotlib.pyplot as plt
from pandas import *
y_axs=''

x_axs=''
sch=read_csv('/home/preethi/Desktop/edu/schooldata.csv')
sch[sch.DISTRICT=='TIRUPUR']

sch[['DISTRICT','PRIMARY SCHOOL','UPPER PRIMARY SCHOOL','SECONDARY SCHOOL ','HIGHER SECONDARY SCHOOL']


sch.plot(kind='barh',x='DISTRICT')
plt.show()

