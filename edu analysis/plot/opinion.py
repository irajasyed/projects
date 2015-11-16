import matplotlib.pyplot as plt
from pandas import *
common_enroll=read_csv('/home/preethi/Desktop/edu/growth/opinion.csv')
#common_enroll[common_enroll[States]==Tamilnadu].plot(kind='pie')
#common_enroll[['Opinion of Children : Quality of Meal (in percent) - Good','Opinion of Children : Quality of Meal (in percent) - Average','Opinion of Children : Quality of Meal (in percent) - Poor']].plot(kind='barh')(
common_enroll.plot(kind='barh',x='States')


plt.show()
