import math

def h(theta_i, x_i):
    return sum([theta_d*x_d for theta_d,x_d in zip(theta_i,x_i)])


def J(theta,x,y):
    return ( sum([ math.pow((h(theta, x_i)-y_i),2) for (x_i, y_i) in zip(x,y) ])  )/2.0


X = []
        # ø_0  ø_1
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

theta = [1.0, 1.0] # loss should be zero
theta = [0.5, 1.5] # loss should be zero

print(J(theta,X,Y))


