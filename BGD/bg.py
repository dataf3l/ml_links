# Batch gradient descent
h_data = [[10, 2], [12, 2], [15, 3], [8, 1]]
y_price = [200, 210, 300, 180]

#print(y_price)

def cal_error(p_vals, y_vals, h_vals):
  difference = []
  for p, y in zip(p_vals, y_vals):
    difference.append(y-p)
 # print(p_vals)
 # return difference
  # uptil n
  tot_sum = 0 
  count = 0
  pro = []
  for  t in h_vals[0]: 
    for i_x, i_dif in zip(h_vals, difference):
      tot_sum = tot_sum + (i_x[count]*i_dif)
    pro.append(tot_sum)
    tot_sum = 0
    count = count+1
  return(pro)
    
    
  
   
def update (errors, alpha, weights):
   updated_weight = []
   for weight, error in zip(weights, errors):
     updated_weight.append(weight-(alpha*error))
   return updated_weight
  
  

  
def predict(weights, data_points):
  predictions = []
  tot_sum = 0
  for data_point in data_points:
    count = 0
    for weight in weights:
      tot_sum = tot_sum+weight*data_point[count]
      count = count+1
    predictions.append(tot_sum)
    tot_sum = 0
  return predictions 

def bg(data, y_val):
  weights = [0.5]*len(h_data[0])
  epoch = 10
  alpha = 2
  for i in range(epoch):
    predictions = predict(weights, data)
    errors = cal_error(predictions, y_val, data)
    weights = update(errors, alpha, weights)
  return (predict(weights, data))  
 

print(y_price)
print(bg(h_data, y_price))
  


