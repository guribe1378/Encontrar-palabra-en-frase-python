"""
Función para encontrar una palabra en un párrafo dado, 
donde se contaran la cantidad de veces que aparece la
palabra en el párrafo, es caso sensitivo, en esta ocasión se convierte 
el párrafo completo a minúscula
"""
def buscapalabra(parrafo,palabra):
    parrafo=input("Ingresa el párrafo:  ")
    palabra=input("Buscar palabra: ")
    test=parrafo.lower()
    encontradas=test.count(palabra)
    print("La cantidad de palabras encontradas como " + "'" + str(palabra) +"'" + " son: " + str(encontradas))

buscapalabra("parrafo","palabra") 