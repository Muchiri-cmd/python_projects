import matplotlib.pyplot as plt

x_values=list(range(1,5))
y_values=[x**3 for x in x_values]
plt.plot(x_values,y_values,linewidth=5)

#set chart title and axis titles
plt.title('Cubes',fontsize=24)
plt.xlabel('values',fontsize=14)
plt.ylabel('cube of values',fontsize=14)

#edit tick parameters
plt.tick_params(axis='both',labelsize=14)
plt.show()