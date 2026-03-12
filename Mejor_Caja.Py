#Title#
print ("Este progama calcula el volumen maximo posible de hacer con una plancha de carton de carton")

#variables

high = float (input("ingresa la altura de tu plancha de carton en centimetros "))
length = float (input("ingresa la longitud de tu plancha de carton en centimetros ")) 
alt = 0.1
V1 = (high-(alt*2))*(length-(alt*2))*alt
V2 = 0

#While

while(V2<V1):
    V2 = V1
    alt+=0.1
    V1=(high-(alt*2))*(length-(alt*2))*alt

#Salida

print("el volumen max es: ", V2 ,"Cm3")

print( "y la altura es: ",alt-0.1,"cm ")


