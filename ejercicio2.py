texto="un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
ask=input("Buen dialogo aunque basatente feo de leer mejor vamos a ordenarlo, no?")
def poesia(texto):
    primera_parte=texto[:39]
    segunda_parte=texto[40:91]
    tercera_parte=texto[92:142]
    cuarta_parte=texto[143:]
    b=primera_parte[1:]
    a=primera_parte[0].upper()
    print(a+b+ "...")
    print("-"+segunda_parte)
    print("-"+tercera_parte)
    print("-"+cuarta_parte)
if ask=="si":
    print("Buena decisión aqui lo tienes")
    print(" ")
    poesia(texto)
else:
    print("Eres un cutre")



