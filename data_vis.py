# Data visualisation --> visual representation to explore 
# and present patterns in datasets
# effective data visualizaion --> makes information look nice
#                             --> meaning becomes clear to viewers

# installing matplotlib
# python3 -m pip install matplotlib

#plotting asimple line graph 
import matplotlib.pyplot as plt

cubes=[1,8,27,64,125]
fig, ax=plt.subplots()
ax.plot(cubes)

plt.show()