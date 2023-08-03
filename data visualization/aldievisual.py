from aldie import Die
import pygal

#create a D6
die=Die()
 
#make some rolls and store results in a list 
results=[]
results.extend(die.roll() for roll_num in range(1000))
    
#Analyze the results 
frequencies=[]
frequency=[results.count(value) for value in range(1,die.num_sides+1)]
frequencies.append(frequency)
    
#visualize the results 
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(1,die.num_sides+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies[0])
hist.render_to_file('die_visual3.svg')