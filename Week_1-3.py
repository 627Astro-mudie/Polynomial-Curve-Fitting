from turtle import color
import numpy as np
import matplotlib.pyplot as plt

x,data=np.loadtxt('noisy_data.txt',unpack=True)

def polynomial(a1,a2):
    x=np.linspace(1.5,5,1000)
    f2 = a1*x +a2*x**2
    return f2

def nestedloop ():
    rms_list = []
    grid =[]
    a1 =np.linspace(0,4,10)
    a2 =np.linspace(-2,2,10)
    for a1_values in a1:
        for a2_values in a2:
            grid.append([a1_values,a2_values])
            value=polynomial(a1_values,a2_values)
            RMS = (np.sqrt(np.sum((data-value)**2)))
            rms_list.append(RMS)
            (((rms_list)))
            rms_array = np.array(rms_list)
            min_rms = np.argmin(rms_array)
    plt.plot(x,data,color = 'red')
    plt.plot(x,value,color ='blue')
    plt.xlabel("Value of x")
    plt.ylabel("Data")
    plt.legend("Best fit")
    plt.show()
    print("These values are best fitting:")
    return grid[min_rms]
print(nestedloop ())

