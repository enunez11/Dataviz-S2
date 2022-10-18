import matplotlib.pyplot as plt
plt.close()

Days = [1,2,3,4,5]
Temps = [23.5, 28.5, 17.5, 20.5, 18.9]
size = [23.5, 28.5, 17.5, 20.5, 18.9]
plt.scatter(x=Days, y=Temps, s=size)
plt.show()