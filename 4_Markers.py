# Markers : You can use the keyword argument marker to emphasize each point with a specified marker (marker = 'sign')
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = '*')
# plt.show()
# ------------------------------------------------------------------------------------------------------------------------------

# Format Strings fmt : You can also use the shortcut string notation parameter to specify the marker. This parameter is also called fmt, and is written with this syntax:
# marker|line|color
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'x:b') # b - blue color, : means dotted line
# plt.plot(ypoints,'*-r') # r - red color, - means solid line

# ms -> marker size
# You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
# plt.plot(ypoints,'o--g', ms=20, mec='r')  
# You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
plt.plot(ypoints, marker='o', ms=20, mfc='b', mec='r')     
plt.show()