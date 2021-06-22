import matplotlib.pyplot as pt
import random
import numpy as np

x = [random.randint(1, 100) for i in range(5)]
y = [1, 8, 10, 15, 9]
# x1 = [random.randint(1, 100) for i in range(10)]
# y1 = [random.randint(1, 100) for i in range(10)]

# normal plot
# font1 = {'family': 'serif', 'color': 'red', 'size': 20}
font2 = {'family': 'serif', 'color': 'black', 'size': 15}
# pt.plot(y, "o:c", ms=10, mec='r', mfc="r", linestyle="dashed")
# pt.xlabel("x - axis", fontdict=font2)
# pt.ylabel("y - axis", fontdict=font2)
# pt.title("Demo Graph", loc="center", fontdict=font1)
# # pt.text(2, 17, "Demo Graph", horizontalalignment="center",fontsize=20,color="red")
# pt.grid(axis="y", color="blue", linestyle='--', linewidth=1)
# pt.show()

# subplot
# pt.subplot(2,3,1)
# pt.plot(x)
# pt.title("1")
# pt.subplot(2,3,2)
# pt.plot(y)
# pt.title("2")
# pt.subplot(2,3,3)
# pt.plot(x)
# pt.title("3")
# pt.subplot(2,3,4)
# pt.plot(y)
# pt.title("4")
# pt.subplot(2,3,5)
# pt.plot(y)
# pt.title("5")
# pt.subplot(2,3,6)
# pt.plot(y)
# pt.title("6")
# pt.show()

# scatterplot and colormap
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70])
# pt.scatter(x, y, c=colors, cmap='ocean')
# pt.colorbar()
# pt.scatter(x1, y1, c=colors, cmap='rainbow')
# pt.colorbar()
# pt.show()


# bar plot
# x = ["A", "B", "C", "D"]
# y = [200, 100, 500, 300]
# pt.bar(x, y,width=1)
# pt.barh(x,y)
# pt.show()


# histogram plot
# x = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8]
# pt.hist(x)
# pt.show()


# pie plot
x = [2, 1.5, 1.75, 2.5]
labels = ["India", "US", "China", "Pakistan"]
textprops = {"fontsize": 12}
pt.pie(x, labels=labels, startangle=0, explode=[0.1, 0, 0, 0], shadow=False, textprops=textprops)
pt.legend(title="Countries",loc="lower left")
pt.show()
