import math
import matplotlib.pyplot as plt

def h(theta, x_i):
    return sum([theta_d*x_d for theta_d,x_d in zip(theta,x_i)])

# LOSS:
def J(theta,x,y):
    return ( sum([ math.pow((h(theta, x_i)-y_i),2) for (x_i, y_i) in zip(x,y) ])  )/2.0

def DJ(theta,x,y):
    return (h(theta,x)-y) * x_j

# generates points on a circle
def gen_circ_points(x, y, radius=100):
    y_low = y-(radius/2)
    y_high = y+(radius/2)
    arr = []
    for i in range(y_low, y_high):
        x_point = ( math.sqrt((math.pow(radius, 2))-(math.pow((y-i), 2)) ))
        arr.append((x_point, i))
    return arr

def Dif_theta_plot():
    theta_start_arr = gen_circ_points(5, 5, 8)
    #print theta_start_arr
    # take each theta run model on it get points and plot on a single graph
    for theta in theta_start_arr:
        theta_plots = main(list(theta))
        #print(theta_plots)
        #for points in theta_plots:
            #print(points[0], points[1])
        x_list = []
        y_list = []
        for points in theta_plots:
            x_list.append(points[0])
            y_list.append(points[1])
        print(x_list)
        print(y_list)
        plt.plot(x_list, y_list, 'bo')
        print("completed one cycle")
        plt.show()
    print("completed")



# make a regression class which takes in theta and gives out a final theta also # can give in all points in an epchos
# make another plotter class which plots the points 


def main(theta = [0.1, 0.1]):
    global Y, X
    epochs = 1000
          # j=0  j=1
    #theta = [0.1, 0.1]
    alpha = 0.01 # learning rate
    loss_values = []
    theta_arr = []
    for epoch in range(0,epochs):
        i = 0
        for x_i in X:
            #print("---------x_" + str(i))
            j = 0   # index
            for theta_j in theta:
                #print("  ---------theta_" + str(j))
                Y_i = Y[i]
                theta[j] = theta_j + alpha * (Y_i - h(theta,x_i)) * x_i[j]
                j += 1
            i += 1
        #print(theta)
        theta_arr.append([theta[0], theta[1]])
        loss = J(theta,X,Y)
        #print("LOSS:",loss)
        loss_values.append(loss)

    #plt.plot(loss_values)
    #plt.show()
    return theta_arr

X = []
        # theta_0  theta_1
X.append([0,    0])
X.append([0.2,  0.2])
X.append([0.6,  0.6])
X.append([0.81,  0.8])
X.append([1.0,  1.0])


Y = []
Y.append(0)
Y.append(0.4)
Y.append(1.2)
Y.append(1.55)
Y.append(2.0)

#theta = [1.0, 1.0] # loss should be zero
#theta = [0.5, 1.5] # loss should be zero

#print(J(theta,X,Y))

main()
Dif_theta_plot()

