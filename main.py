colombia_words = {
    "Gallina": "Persona cobarde",
    "Mano": "Es un amigo/compañero",
    "Rumbear": "Ir a una fiesta o salir a bailar",
    "Bacano": "Algo que es excelente o impresionante",
}

word = input("Escribe una palabra que no entiendas: ")

if word in colombia_words.keys():
    print("El significado de '" + word + "' es: " + colombia_words[word])
else:
    print("Lo siento, no conozco el significado de '" + word + "'.")
