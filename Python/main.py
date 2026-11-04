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
buscar_tecnologia("python")

def agregar_candidatos(nuevo_candidato):
    candidatos.append(nuevo_candidato)

agregar_candidatos(candidato4)
print(candidatos)

def buscar_id(id_buscado):
    for candidato in candidatos:
        if candidato["id"]== id_buscado:
            print([candidato])
buscar_id(3)