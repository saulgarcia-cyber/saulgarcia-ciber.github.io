import random

# Listas de notas y tipos de acordes
notas = ["C", "C                                                         
tipos_acordes = ["#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
tipos_acordes = ["Mayor", "Menor", "7ª", "Maj7"]

                                           
def generar_acorde():
    nota = random.choice(notas)
    tipo_acorde = random.choice(tipos_acordes)
    return f"# Función para generar un acorde aleatorio
def generar_acorde():
    nota = random.choice(notas)
    tipo_acorde = random.choice(tipos_acordes)
    return f"{nota} {tipo_acorde}"

                                       
acorde = generar_acorde()
print(f"# Generar y mostrar el acorde aleatorio
acorde = generar_acorde()
print(f"El acorde aleatorio generado es: {acorde}")
