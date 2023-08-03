import matplotlib.pyplot as plt
from get_step import RandomWalk 


while True:
    #make a random walk and print the points
    gs=RandomWalk()
    gs.fill_walk()
    #set plotting window size
    plt.figure(dpi=128,figsize=(10,6))
    
    
    point_numbers=list(range(gs.num_points))
    plt.scatter(gs.x_values,gs.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(gs.x_values[-1], gs.y_values[-1], c='red', edgecolors='none',
    s=100)
   
    # Remove the axes.
    ax = plt.gca()#gets current axes of the object or creates
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    
    plt.show()

    keep_running=input("take another walk ? (y/n):")
    if keep_running== 'n':
        break