import matplotlib.pyplot as plt

x_values=list(range(5001))
y_values=[x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=10)

#set chart title and axis labels
plt.title('cubes')
plt.xlabel('values')
plt.ylabel('cubes of values')

#select graph range and save png ouput
plt.tick_params(axis='both',labelsize=14)
plt.axis([0,5001,0,5001**3])
plt.show()