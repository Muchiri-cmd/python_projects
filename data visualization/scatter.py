import matplotlib.pyplot as plt
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

#set chart title and label axes
plt.title("square numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)

#set range size for each axis 
plt.axis([0,1100,0,1100000])
plt.savefig('squares_plot.png',bbox_inches='tight')