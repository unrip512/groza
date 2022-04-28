import time
import matplotlib.pyplot as plt
import numpy as np

with open ("/home/b01-109/data.txt", "r") as data:
    tmp = [ int(i)*3.3/255 for i in data.read().split("\n")]

x = np.arange(0, 900, 10)
y = np.arange(0, 3.5, 0.1)


fig, ax = plt.subplots()
ax.plot(tmp, "darkcyan", label="V(t)") # построить график цвета  темный циан 
ax.plot(tmp, 'o', markevery = 20, color = 'darkcyan') #сделать  маркировку графика
ax.grid(which = 'major',color = 'k', linewidth = 1) # добавить основные оси черного цвета 
ax.minorticks_on() # включить второстепенные деления осей
ax.set_title('Процесс заряда и разряда конденсатора в RC - цепочке') # название графика

ax.grid(which='minor', 
        color = 'k', 
        linestyle = ':') # добавить второстепенные оси в сетке

fig.set_figwidth(12) # задать ширину графика
fig.set_figheight(6) #задать высоту графика

plt.ylabel("Напряжение, В") #подписать ось x
plt.xlabel("Время, сек") #  подписать ось y

plt.text(0, 7, "HELLO!", fontsize=15) #тесктовый блок на поле графика

box_1 = {'facecolor':'gainsboro',    #  цвет области
       'edgecolor': 'dimgrey',     #  цвет крайней линии
       'boxstyle': 'round'}    #  стиль области

ax.text(600, 2, ' Время заряда 4,21 c \n Время разряда 5,65 сек',
        bbox = box_1,
        color = 'black',    #  цвет шрифта
        fontsize = 10)

ax.legend(loc="upper right", title="Legend title")



fig.savefig("/home/b01-109/laba.png")
plt.show()



