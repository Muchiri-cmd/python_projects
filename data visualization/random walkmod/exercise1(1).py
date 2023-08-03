import matplotlib.pyplot as plt
x_values=[1,2,3,4,5]
y_values=[1,8,27,64,125]
plt.scatter(x_values,y_values,edgecolor='none',s=40)

#set chart title and axis labels
plt.title('Cubes',fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('cubes of values',fontsize=14)

#set up plot and scatter
plt.tick_params(axis='both',labelsize=14)
plt.show()