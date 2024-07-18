# Creating Pie Charts
# With Pyplot, you can use the pie() function to draw pie charts
# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# plt.pie(y) # y means AntiClockWise Direction
# plt.show() 




# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# # The startangle parameter is defined with an angle in degrees, default angle is 0
# plt.pie(y, labels = mylabels, startangle = 90)
# plt.show() 



# Explode
# Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.
# The explode parameter, if specified, and not None, must be an array with one value for each wedge.
# Each value represents how far from the center each wedge is displayed
# To Add a shadow to the pie chart by setting the shadows parameter to True.
# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]
# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
# plt.show() 




# You can set the color of each wedge with the colors parameter.
# The colors parameter, if specified, must be an array with one value for each wedge
# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# mycolors = ["black", "hotpink", "b", "#4CAF50"]
# plt.pie(y, labels = mylabels, colors = mycolors)
# plt.show() 




# Legend
# To add a list of explanation for each wedge, use the legend() function
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 