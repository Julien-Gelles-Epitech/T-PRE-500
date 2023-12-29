import sys, math
import numpy as np
import matplotlib.pyplot as plt

#Task01
#create a list of 100 evenly spaced numbers between 0 and 100
x_values = np.linspace(0 ,100, 100, endpoint=False, dtype=int)

#Task02
points = [(0,12), (1,32), (2,42), (3,52)]
# plt.xlim(-0.2, 3.2)
# plt.ylim(10, 54)
# plt.margins(x=2, y=2)
# plt.grid()
# for p in points:
#     plt.plot(p[0], p[1], marker="o", markersize=7, markeredgecolor="red", markerfacecolor="red")
# plt.show()

#Task03
def task03(points):
    for point in points:
        plt.plot(point[0], point[1], marker="o", markersize=7, markeredgecolor="red", markerfacecolor="red")
    plt.grid()
    plt.show()

#Task04
def plot_fct(fct, start, end, pas=1):
    x,y=[],[]
    for i in np.arange(start, end+1, pas):
        x.append(i)
        y.append(fct(i))
    plt.plot(x, y)
    plt.grid()
    plt.show()

def f(x):
    return x**2+x*3+2
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                print("Create a list of 100 evenly spaced numbers between 0 and 100")
            case '02':
                for p in points:
                    plt.plot(p[0], p[1], marker="o", markersize=7, markeredgecolor="red", markerfacecolor="red")
                plt.grid()
                plt.show()
            case '03':
                task03([(1,2), (2,1), (3,3), (4,4)])
            case '04':
                plot_fct(math.sin, 0, 50, 0.1)
                plot_fct(f, -100, 200)
                plot_fct(lambda x:x**2, -10, 10)
                plot_fct(lambda x:1/x, -100, 100)
