import colorama
from colorama import Fore,Back,init
init()

banner = """


                                     $     $   $$$$$$$$$    $$$$$$$$$$    $$$$$$$$$$
                                     $    $    $           $             $
                                     $   $     $           $             $
                                     $  $      $           $             $
                                     $ $       $$$$$$$$$   $             $
                                     $ $       $           $             $
                                     $  $      $           $  $$$$$$$$   $   
                                     $   $     $           $         $   $
                                     $    $    $           $         $   $
                                     $     $   $$$$$$$$$    $$$$$$$$$$    $$$$$$$$$$


"""
menu ="""

                   ____________________________________________________________________________________
 
                            =========================KEGC/EXTRA AVANZADA===============================
                   ____________________________________________________________________________________



"""
line = 1
while line ==1:
	print(Fore.MAGENTA+banner)
	print(Fore.MAGENTA+menu)
	break


print("Metodo avanzado: sirve para toda clase de bins de 6 numeros, 7 numeros, 8 numeros etc")
print(" ")
print("Instrucciones: ")
print(" ")
print("Ocupas 2 lives del bin que quieres sacarle extra ")
print(" ")
print("Divide tu live en 4 partes ")
print(" ")
print("Ejemplo: ")
print(" ")
print("live1: 5470 4645 7655 4954 , live2: : 5470 4638 5657 4654 ")
print(" ")
print("Ahora solo agarras los 2 numeros del medio de la tercera parte 5655 = x65x , 5657 = x65x")
print(" ")
print("Tienes que poner abajo los 9 numeros de tu live y 2 ceros" )
print(" ")
print("Ejemplo: live1: 54704645700 , live2: 54704638500" )
print(" ")
print("Has lo de abajo")
print(" ")
bin1 = int(input("coloca los primeros 9 numeros de tu primera live aqui y 2 ceros: "))
bin2 = int(input("coloca los primeros 9 numeros de tu segunda live aqui y 2 ceros: "))
print(" ")
suma1 = int(input("Coloca tu numero de la derecha de los 2 numeros que sacamos al principio de tu primera live: "))
suma2 = int(input("Coloca tu numero de la derecha de los 2 numeros que sacamos al principio de tu segunda live: "))
print(" ")
suma3 = int(input("Coloca tu numero de la izquierda de los 2 numeros que sacamos al principio de tu primera live: "))
suma4 = int(input("Coloca tu numero de la izquierda de los 2 numeros que sacamos al principio de tu segunda live: "))
print(" ")
suma = suma1 + suma2
Suma = suma3 + suma4
divi1 = suma/2
divi2 = Suma/2
multi1 = divi1 * 5
multi2 = divi2 * 5
suma5 = multi1 + multi2
print(bin1 + int(suma5))
print(bin2 + int(suma5))
print(" ")
print("Ahora solo tendras que copiar los 2 bins de arriba y ponerle las x")
 





       


           
    
                     









