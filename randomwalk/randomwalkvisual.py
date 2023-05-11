import matplotlib.pyplot as plt
from randomwalk import RandomWalk 

while True:
    #make a random walk and print the points
    rw=RandomWalk()
    rw.fill_walk()
    #set plotting window size
    plt.figure(dpi=128,figsize=(10,6))
    
    
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)
   
    # Remove the axes.
    ax = plt.gca()#gets current axes of the object or creates
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    
    plt.show()

    keep_running=input("take another walk ? (y/n):")
    if keep_running== 'n':
        break
