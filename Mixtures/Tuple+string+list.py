test_list = ["python", "is"] 

test_str = "best"

# printing original list and tuple 

print("The original list : " + str(test_list)) 

print("The original string : " + test_str) 

# Construct tuple from string and list 
# using list conversion to tuple + tuple() 

res = tuple(test_list + [test_str])

print("The aggregated tuple is : " + str(res)) 

# Below is the Output :

The original list : ['python', 'is']
The original string : best
The aggregated tuple is : ('python', 'is', 'best')
