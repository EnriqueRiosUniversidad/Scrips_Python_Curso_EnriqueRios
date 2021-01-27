#Bloque de carga de precio
p_lechuga   = 3000
p_perejil   = 1500
p_berenjena = 4500
p_tomate    = 700
#Cuanto quiere comprar el usuario
c_lechuga     = eval(input("Ingrese numero de lechugas: "))
c_perejil     = eval(input("Ingrese numero de perejiles: "))
c_berenjena   = eval(input("Ingrese numero de berenjenas: "))
c_tomate      = eval(input("Ingrese numero de tomate: "))
#operaciones
costo  = (p_lechuga*c_lechuga)+(p_perejil*c_perejil)+(p_berenjena*c_berenjena)+(p_tomate*c_tomate)
saldo  = eval(input("Ingrese el dinero que dispone"))
vuelto = saldo-costo
#mostramos el vuelto
print ("su vuelto es: ", vuelto)
                   
