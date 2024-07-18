# Display Multiple Plots : With the subplot() function you can draw multiple plots in one figure
# import matplotlib.pyplot as plt
# import numpy as np
# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)    # 1 row, 2 col, 1st plot
# plt.plot(x,y)
# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)    # 1 row, 2 col, 2nd plot
# plt.plot(x,y)
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 3, 1)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 3, 2)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 3, 3)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 3, 4)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 3, 5)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 3, 6)
# plt.plot(x,y)



# You can add a title to each plot with the title() function:
import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")
plt.show()




