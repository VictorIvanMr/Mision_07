#Victor Ivan Morales Ramos A01377601
#Descripcion: Crear un menu para dos tipos de operaciones diferentes.

def dividir(dividendo,divisor):
    a = dividendo
    b = divisor
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo-divisor
        cociente+=1

    return print(a, "/" , b , " = ", cociente, ", sobra ", dividendo)

def encontrarMayor():
   print("Teclea una serie de numeros para encontrar el mayor.")
   x = int(input("Teclea un numero [-1 para salir]: "))
   if x != -1:
       vm = 0
       while x != -1:
           if x >= vm:
               vm = x
           x = int(input("Teclea un numero [-1 para salir]: "))
       print("El valor mayor es: " , vm)
   else:
       print("No hay un valor mayor")



def main():
    menu = int(input("""
Mision 07: Ciclos While
Autor: Victor Ivan Morales Ramos
Matricula: A01377601
1. Calcular divisiones.
2. Encontrar el mayor.
3. Salir.
Teclea tu opcion: """))

    while menu !=3:
        if menu == 1:
            print("Calculando divisiones")
            #///////////////////////////////////////////////////////#
            dividendo = int(input("Dame el valor del dividendo: ")) #
            divisor = int(input("Dame el valor del divisor: "))     #DIVISIONES
            dividir(dividendo, divisor)                             #
            #///////////////////////////////////////////////////////#
            menu = int(input("""
Mision 07: Ciclos While
Autor: Victor Ivan Morales Ramos
Matricula: A01377601
1. Calcular divisiones.
2. Encontrar el mayor.
3. Salir.
Teclea tu opcion: """))

        elif menu == 2:
            print("Calculando Mayor")
            encontrarMayor()
            menu = int(input("""
Mision 07: Ciclos While
Autor: Victor Ivan Morales Ramos
Matricula: A01377601
1. Calcular divisiones.
2. Encontrar el mayor.
3. Salir.
Teclea tu opcion: """))
        else:
            print("ERROR, teclea 1, 2 o 3")
            menu = int(input("""
Mision 07: Ciclos While
Autor: Victor Ivan Morales Ramos
Matricula: A01377601
1. Calcular divisiones.
2. Encontrar el mayor.
3. Salir.
Teclea tu opcion: """))
    print("Gracias por usar este programa, regresa pronto :D.")
main()
