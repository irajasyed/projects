import matplotlib.pyplot as plt
from pandas import *
y_axs=''

x_axs=''
tc=read_csv('/home/preethi/Desktop/edu/teach/higher_sec_rural_urban_2009.csv')
xx=tc[tc['STATE/U.T.']=='Goa']
xx.plot(kind='bar')
plt.legend(loc='best')
plt.show()
#print xx[xx.'Full Time Teachers - Male']]

#sch[['DISTRICT','PRIMARY SCHOOL','UPPER PRIMARY SCHOOL','SECONDARY SCHOOL ','HIGHER SECONDARY SCHOOL']


#sch.plot(kind='barh',x='DISTRICT')
#plt.show()

