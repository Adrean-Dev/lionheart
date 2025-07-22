from google import genai

#List of sprites
sprites = [
    "cielo",
    "suelo",
    "sol",
    "luna",
    "persona",
    "árbol",
    "ave"
]

#Creating the first part of AI request
temp = "Simplemente genera (sin código) una lista Python 16x16 (en una línea) que represente una imagen, con las siguientes claves:"
temp = " ".join([temp,f"{sprites[0]}=0"])

for i in range(1, len(sprites)):
    temp = ", ".join([temp,f"{sprites[i]}={i}"])

#Requesting User input (Vale tiene que escribir algo :P)
msg = input("Tú: ")

#Compiling the full AI request
msg = temp + f". El texto es: \"{msg}\" Si detectas que faltan claves para generar la lista, añade su número y dime qué etiqueta le pondrías (también en una lista Python)."

#Creating AI Client with gemini API (bautizado como Geluropoda molamola II)
main = genai.Client(api_key="AIzaSyCBkJtzJ2BfROl4cMbdqBQe2V2lAbsj9ZQ")
#Sending request to Geluropoda molamola II
response = main.models.generate_content(model="gemini-2.5-flash", contents=msg)

objects = response.text.split("`")
print(objects)

matrix = None
failed = None
i = 0
for obj in objects:
    if 'python\n' in obj:
        if i == 0:
            matrix = obj[7:-1]
            i = 1
            continue
        failed = obj

print(f"Matriz: {matrix}\n\nDatos:{failed}")
print(list(matrix))