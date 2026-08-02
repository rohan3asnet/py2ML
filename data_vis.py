# Data visualisation --> visual representation to explore 
# and present patterns in datasets
# effective data visualizaion --> makes information look nice
#                             --> meaning becomes clear to viewers

# installing matplotlib
# python3 -m pip install matplotlib

#plotting asimple line graph 
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