import math
import matplotlib.pyplot as plt

def h(theta, x_i):
    return sum([theta_d*x_d for theta_d,x_d in zip(theta,x_i)])

# LOSS:
def J(theta,x,y):
    return ( sum([ math.pow((h(theta, x_i)-y_i),2) for (x_i, y_i) in zip(x,y) ])  )/2.0

def DJ(theta,x,y):
    return (h(theta,x)-y) * x_j

def main():
    global Y, X
    epochs = 10
          # j=0  j=1
    theta = [0.1, 0.1]
    alpha = 0.1 # learning rate
    loss_values = []
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
        loss = J(theta,X,Y)
        print("LOSS:",loss)
        loss_values.append(loss)

    plt.plot(loss_values)
    plt.show()

X = []
        # theta_0  theta_1
X.append([0,    0])
X.append([0.2,  0.2])
X.append([0.6,  0.6])
X.append([0.8,  0.8])
X.append([1.0,  1.0])


Y = []
Y.append(0)
Y.append(0.4)
Y.append(1.2)
Y.append(1.6)
Y.append(2.0)

#theta = [1.0, 1.0] # loss should be zero
#theta = [0.5, 1.5] # loss should be zero

#print(J(theta,X,Y))

main()

