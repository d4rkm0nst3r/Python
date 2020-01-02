import math
 
max=21
separacion=5
j=1
 
# creamos el arbol
for i in range(0,max,2):
 
    # ponemos los espacios
    linea=(separacion+math.ceil(max/2)-j)*" "
 
    # ponemos los asteriscos
    linea+=i*"*"
 
    j+=1
    print(linea)
 
# cramos el tronco
linea=(separacion+math.ceil(max/2)-3)*" "
linea+=4*"*"
print(linea)
print(linea)