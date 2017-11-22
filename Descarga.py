import requests
url = "https://twitter.com/EPN"
info = requests.get(url)

listaLineas = info.text.split("\n")

linea = listaLineas[0]
indice = 0
while 'hiddenVisually">Seguidores' not in linea:
    indice += 1
    linea = listaLineas[indice]

print("************",linea)
cadena = listaLineas[indice+1]
print(cadena)
tokens = cadena.split("=")
datos = tokens[2].split()
numeroSeguidores = int(datos[0])
print("Seguidores: ", numeroSeguidores)

seguidores = cadena[cadena.index("t=")+2:cadena.index(" data-is")]
print(seguidores)


#  Buscar tweets
for linea in listaLineas:
    if "TweetTextSize" in linea:
        cadena = linea[linea.index(">")+1:]
        print(cadena)
        mensaje = ""
        agrega = True
        for letra in cadena:
            if letra=="<":
                agrega = False
            if letra==">":
                agrega = True
                mensaje += " "
                continue
            if agrega:
                mensaje += letra
        while "  " in mensaje:
            mensaje = mensaje.replace("  ", " ")
        print(mensaje)

