"""
enunciado
"""
#tabla = 5
tabla = int(input("Dime el númoro de la tabla "))

# range(11) -> range(0, 11, 1)  -> empieza por 0, y el numero llega hasta x-1
for i in range(11):
    #print(i)
    print(str(tabla) + " x " + str(i) + " = " + str(tabla * i))