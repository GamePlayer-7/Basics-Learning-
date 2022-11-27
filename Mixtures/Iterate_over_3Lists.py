import itertools  # Itertool is a module that provides various functions that work on iterators to produce complex iterators.

num = [1, 2, 3] 

tech = ['Python', 'Java', 'Html'] 

value = [3.7, 19] 

  
# iterates over 3 lists and executes  
# 2 times as len(value)= 2 which is the 
# minimum among all the three  

for (a, b, c) in zip(num, tech, value): 
  print (a, b, c) 
  
# Below is the Output : 

1 Python 3.7
2 Java 19
