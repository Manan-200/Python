import random
import math

layer1 = []
layer2 = []
e = 2.7182818
batch_size = 5
X_list = [[2, 9], [9, 2]]
  
#left, right = [0, 1]

#Node class
class Node:
  def __init__(self, inputs):
    self.weights = []
    for i in range(inputs):
      self.weights.append(random.randint(1, 5)*(10**-1))
    self.bias = random.randint(1, 5)*(10**-2)
    self.output = 0

#Forward function
def forward(data, layer):
  output = []
  for node in layer:
    output.append(vector_product(data, node.weights) + node.bias)
  return(output)

def vector_product(arr1, arr2):
  output = 0
  for i in range(len(arr1)):
    output += arr1[i]*arr2[i]
  return(output)

#Activation_functions
def ReLU(data):
  output  = []
  for value in data:
    output.append(max(0, value))
  return(output)
  
def softmax(data):
  output = []
  exp_data = []
  for value in data:
    exp_data.append(e**(value - max(data)))
  for value in exp_data:
    output.append(value/sum(exp_data))
  return(output)
  
#Changing weights and biases of a layer  
def randomize(layer):
  for node in layer:
    for weight in node.weights:
      weight += random.randint(1, 10) * (10**-1)
    node.bias += random.randint(1, 4) * (10**-2)

#Clipping 1 and 0 in data
def clip(data):
  for i in range(len(data)):
    if data[i] == 0:
      data[i] = 0.00000000001
    elif data[i] == 1:
      data[i] = 0.9999999999
  return(data)

#Initializing the nn    
for i in range(3):
  layer1.append(Node(2))
for i in range(2):
  layer2.append(Node(3))

#Training the nn
loss_list = [1]
while max(loss_list) > 0.1:
  loss_list = []
  randomize(layer1)
  randomize(layer2)
  for i in range(len(X_list)):
    print("New iteration")
    X = X_list[i]
    #Getting target class
    if X[0] >= X[1]:
      target_class = 0
    else:
      target_class = 1
    
    #Going forward
    print(X)
    layer1_out = ReLU(forward(X, layer1))
    layer2_out = forward(layer1_out, layer2)
    print(layer2_out)
    layer2_out = clip(softmax(layer2_out))
    print(layer2_out)
    
    loss = -math.log(layer2_out[target_class])
    print(loss)
    loss_list.append(loss)
    if loss > 0.1:
      continue

#Running trained nn on random output
for i in range(10):
  X = [random.randint(1, 10), random.randint(1, 10)]
  if X[0] >= X[1]:
    target_class = 0
  else:
    target_class = 1
  layer1_out = ReLU(forward(X, layer1))
  layer2_out = clip(softmax(forward(layer1_out, layer2)))
  loss = -math.log(layer2_out[target_class])
  print(X, layer2_out)
  print(loss)
