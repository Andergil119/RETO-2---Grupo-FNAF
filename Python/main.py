import json

candidato1 = {
    "id":1,
    "nombre": "Juan",
    "apellidos":"Perez Garcia",
    "puesto":"programador",
    "tecnologia":"python",
    "experiencia":4
}

candidato2 = {
    "id":2,
    "nombre": "Alvaro",
    "apellidos":"Benito Lopez",
    "puesto":"diseñador web",
    "tecnologia":"html",
    "experiencia":2
}

candidato3 = {
    "id":3,
    "nombre": "Alfonso",
    "apellidos":"Martin Aramburu",
    "puesto":"programador",
    "tecnologia":"python",
    "experiencia":3
}

candidato4= {
    "id":4,
    "nombre": "Unai",
    "apellidos":"Etxeberria Jimenez",
    "puesto":"programador",
    "tecnologia":"java",
    "experiencia":5
}

candidatos =[candidato1, candidato2, candidato3]

def buscar_tecnologia(tecnologia_buscada):
    for candidato in candidatos:
        if candidato ["tecnologia"] == tecnologia_buscada:
            print([candidato])

def agregar_candidatos(nuevo_candidato):
    candidatos.append(nuevo_candidato)


def buscar_id(id_buscado):
    for candidato in candidatos:
        if candidato["id"]== id_buscado:
            print([candidato])

def eliminar_candidato(id_buscado):
    for candidato in candidatos:
        if candidato["id"]==id_buscado:
            candidatos.remove(candidato)
            print("El candidato",[candidato], "fue eliminado correctamente.")

def guardar_datos():
    with open("candidatos.json","w",encoding="utf-8") as archivo:
        json.dump(candidatos, archivo, indent=4, ensure_ascii=False)


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
        agregar_candidatos(candidato4)
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
    

