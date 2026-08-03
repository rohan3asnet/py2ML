# Data visualisation --> visual representation to explore 
# and present patterns in datasets
# effective data visualizaion --> makes information look nice
#                             --> meaning becomes clear to viewers

# installing matplotlib
# python3 -m pip install matplotlib

# plotting asimple line graph 
import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
cubes=[1,8,27,64,125]

#to use styles add below line of code beofre calling subplots()
plt.style.use('Solarize_Light2')
fig, ax=plt.subplots()
ax.plot(input_values, cubes, linewidth =3)

#set chart title and label axes
ax.set_title("Cube Numbers", font="Times New Roman",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

#set size of tick lables
ax.tick_params(labelsize=14)

plt.show()

#scatter()

plt.style.use('Solarize_Light2')
fig, ax=plt.subplots()
ax.scatter(3,9, s=200)# s is used to set the size of dots
#set chart titles and labeles
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("square of Value", fontsize=14)
#set size of tick labels
ax.tick_params(labelsize=14)
plt.show()

#plotting a series of points with scatter()
x_values=[1,2,3,4,5,6]
y_values=[1,4,9,16,25,36]

plt.style.use('Solarize_Light2')
fig, ax=plt.subplots()
ax.scatter(x_values,y_values, s=100)
#set chart titles and labeles
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("square of Value", fontsize=14)
#set size of tick labels
ax.tick_params(labelsize=14)
plt.show()

x_values=range(1,100)
y_values=[x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax=plt.subplots()
ax.scatter(x_values,y_values, s=10)
#set chart titles and labeles
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("square of Value", fontsize=14)
#set the range of each axis
ax.axis([0,100, 0,10000])

plt.show()