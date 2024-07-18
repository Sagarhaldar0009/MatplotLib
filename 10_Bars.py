# Creating Bars
# With Pyplot, you can use the bar() function to draw bar graphs
# import matplotlib.pyplot as plt
# import numpy as np
# # x = np.array(["A", "B", "C", "D"])
# # y = np.array([3, 8, 1, 10])
# x = ["APPLES", "BANANAS"]
# y = [400, 350]
# plt.bar(x, y)
# # plt.bar(x,y)
# plt.show()



# Horizontal Bars
# If you want the bars to be displayed horizontally instead of vertically, use the barh() function
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.barh(x, y)
# plt.show()



# Bar Color
# The bar() and barh() take the keyword argument color to set the color of the bars
# The bar() takes the keyword argument width to set the width of the bars
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "red", width=0.1)
plt.barh(x, y, color = "red", height = 0.1)
plt.show()