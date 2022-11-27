string = "{'A':Python, 'B':Java, 'C':Azure}"

  
# eval() convert string to dictionary 

Dict = eval(string) 

print(Dict) 

print(Dict['A']) 

print(Dict['B'])

print(Dict['C']) 

# Below is the Output :

{'A':Python, 'B':Java, 'C':Azure}
Python
Java
Azure
