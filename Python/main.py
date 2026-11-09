import json

with open("candidatos.json", "r", encoding="utf-8") as archivo:
    candidatos = json.load(archivo)

candidato1 = {
    "id":1,
    "nombre": "Juan",
    "apellidos":"Perez Garcia",
    "puesto":"programador",
    "tecnologia":"python",
    "experiencia":4,
    "correo":"juanperez@gmail.com",
    "telefono":611111111
}

candidato2 = {
    "id":2,
    "nombre": "Alvaro",
    "apellidos":"Benito Lopez",
    "puesto":"diseñador web",
    "tecnologia":"html",
    "experiencia":2,
    "correo":"alvarobenito@gmail.com",
    "telefono":622222222
}

candidato3 = {
    "id":3,
    "nombre": "Alfonso",
    "apellidos":"Martin Aramburu",
    "puesto":"programador",
    "tecnologia":"python",
    "experiencia":3,
    "correo":"alfonsomartin@gmail.com",
    "telefono":633333333
}


candidatos =[candidato1, candidato2, candidato3]


# Busca y muestra los candidatos que coincidan con la tecnología que le pidas
def buscar_tecnologia(tecnologia_buscada):
    busqueda_limpia = tecnologia_buscada.strip().lower()

    for candidato in candidatos:
        if candidato ["tecnologia"].lower() == busqueda_limpia:
            print([candidato])

# Pide los datos de una persona nueva y la añade a la lista
def agregar_candidatos():
    nombre = input("Nombre: ").strip()
    apellidos = input("Apellidos: ").strip()
    puesto = input("Puesto deseado: ").strip()
    tecnologia = input("Tecnología dominante: ").strip().lower()
    experiencia = int(input("Años de experiencia: "))
    correo = input("Correo electronico: ").strip()
    telefono = input("Número de teléfono: ")

    nuevo_id=len(candidatos)+1

    nuevo_candidato={
        "id":nuevo_id,
        "nombre":nombre,
        "apellidos":apellidos,
        "puesto": puesto,
        "tecnologia": tecnologia,
        "experiencia": experiencia,
        "correo": correo,
        "telefono": telefono
    }

    candidatos.append(nuevo_candidato)

# Busca y muestra al candidato que tenga el número de ID exacto que busques
def buscar_id(id_buscado):
    for candidato in candidatos:
        if candidato["id"]== id_buscado:
            print([candidato])

# Borra de la lista al candidato que coincida con el ID que le des
def eliminar_candidato(id_buscado):
    for candidato in candidatos:
        if candidato["id"]==id_buscado:
            candidatos.remove(candidato)
            print("El candidato",[candidato], "fue eliminado correctamente.")

# Guarda todos los cambios de los candidatos en un archivo externo de texto (JSON)
def guardar_datos():
    with open("candidatos.json","w",encoding="utf-8") as archivo:
        json.dump(candidatos, archivo, indent=4, ensure_ascii=False)

# Menú principal que se repite hasta que decides salir
while True:
    print("1. Ver todos los candidatos. \n" \
    "2. Buscar por tecnologia. \n" \
    "3. Agregar candidato. \n" \
    "4. Eliminar candidato. \n" \
    "5. Salir")

    opcion_menu=input("Elige una opcion: ")

    if opcion_menu=="1":
        print(candidatos)

    elif opcion_menu=="2":
        tecnologia_buscada=input("¿Que tecnologia buscas? ")
        buscar_tecnologia(tecnologia_buscada)

    elif opcion_menu=="3":
        agregar_candidatos()
        print("Candidato agregado correctamente.")

    elif opcion_menu=="4":
        candidato_eliminado=input("Inserta el id del candidato que quieres eliminar: ")
        eliminar_candidato(int(candidato_eliminado))

    elif opcion_menu=="5":
        print("Cerrando programa...")
        guardar_datos()
        break

    else:
        print("Error. Lo que has introducido no es correcto.")
    

