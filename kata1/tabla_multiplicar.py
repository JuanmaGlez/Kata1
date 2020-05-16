"""
enunciado
"""
#tabla = 5
#tabla = int(input("Dime el númoro de la tabla "))
tabla = input("Dime el númoro de la tabla ")
try:
    tabla = int(tabla)
#    if (isinstance(tabla, int)):
        # range(11) -> range(0, 11, 1)  -> empieza por 0, y el numero llega hasta x-1
    for i in range(11):
        #print(i)
        print(str(tabla) + " x " + str(i) + " = " + str(tabla * i))
except:
    print("Solo vale números")    

