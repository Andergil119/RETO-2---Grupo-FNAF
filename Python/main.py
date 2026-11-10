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
    "telefono":"611111111"
}

candidato2 = {
    "id":2,
    "nombre": "Alvaro",
    "apellidos":"Benito Lopez",
    "puesto":"diseñador web",
    "tecnologia":"html",
    "experiencia":2,
    "correo":"alvarobenito@gmail.com",
    "telefono":"622222222"
}

candidato3 = {
    "id":3,
    "nombre": "Alfonso",
    "apellidos":"Martin Aramburu",
    "puesto":"programador",
    "tecnologia":"python",
    "experiencia":3,
    "correo":"alfonsomartin@gmail.com",
    "telefono":"633333333"
}

# Los candidatos de ejemplo solo se usan si no había datos guardados
if len(candidatos)==0:
    candidatos = [candidato1, candidato2, candidato3]

# Devuelve una lista de candidatos
def mostrar_candidatos(lista, titulo="Candidatos"):
    print(titulo + ":")
    for candidato in lista:
        print("id:", candidato["id"], "|",
              candidato["nombre"], candidato["apellidos"], "|",
              candidato["puesto"], "|",
              candidato["tecnologia"], "|",
              candidato["experiencia"], "años |",
              candidato["correo"], "|",
              candidato["telefono"])

# Busca y devuelve los candidatos que coincidan con la tecnología que le pidas
def buscar_tecnologia(tecnologia_buscada):
    busqueda_limpia = tecnologia_buscada.strip().lower()
    resultado = []

    for candidato in candidatos:
        if candidato ["tecnologia"].lower() == busqueda_limpia:
            resultado.append(candidato)
    return(resultado)

# Pide los datos de una persona nueva y la añade a la lista
def agregar_candidatos():
    nombre = input("Nombre: ").strip()
    apellidos = input("Apellidos: ").strip()
    puesto = input("Puesto deseado: ").strip()
    tecnologia = input("Tecnología dominante: ").strip().lower()
    experiencia =input("Años de experiencia: ").strip()
    while not experiencia.isdigit():
        print("Tienes que escribir un numero entero.")
        experiencia = input("Años de experiencia: ").strip()
    experiencia=int(experiencia)
    correo = input("Correo electronico: ").strip()
    while "@" not in correo:
        print("El correo no es valido.")
        correo = input("Correo electronico: ").strip()
    telefono = input("Número de teléfono: ").strip()
    while not telefono.isdigit() or len (telefono) !=9:
        print("El telefono debe tener 9 numeros.")
        telefono = input("Número de teléfono: ").strip()

    nuevo_id=1
    for candidato in candidatos:
        if candidato["id"]>=nuevo_id:
            nuevo_id = candidato["id"]+1

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

# Busca y devuelven al candidato que tenga el número de ID exacto que busques
def buscar_id(id_buscado):
    for candidato in candidatos:
        if candidato["id"]== id_buscado:
            return candidato
    return None

# Borra de la lista al candidato que coincida con el ID que le des
def eliminar_candidato(id_buscado):
    for candidato in candidatos:
        if candidato["id"]==id_buscado:
            candidatos.remove(candidato)
            print("El candidato",[candidato], "fue eliminado correctamente.")
            return
    print("No existe ningun candidato con ese id.")

# Devuelve las tecnologias diferentes que hay entre los candidatos
def listar_tecnologias():
    tecnologias = set()
    for candidato in candidatos:
        tecnologias.add(candidato["tecnologia"])
    return tecnologias

#Devuelve las tecnologias pedidas que ningun candidato tiene
def tecnologias_sin_candidatos(tecnologia_buscada):
    pedidas = set()
    for tecnologia in tecnologia_buscada.lower().split(","):
        pedidas.add(tecnologia.strip())
    return pedidas - listar_tecnologias()

# Devuelve un diccionario de cuantos candidatos hay por puesto
def contar_por_puesto():
    por_puesto = {}
    for candidato in candidatos:
        puesto = candidato["puesto"].lower()
        por_puesto[puesto] = por_puesto.get(puesto, 0) + 1
    return por_puesto

# Guarda todos los cambios de los candidatos en un archivo externo de texto (JSON)
def guardar_datos():
    with open("candidatos.json","w",encoding="utf-8") as archivo:
        json.dump(candidatos, archivo, indent=4, ensure_ascii=False)

# Crear un informe .txt
def exportar_informe():
    with open("informe_candidatos.txt", "w", encoding="utf-8") as archivo:
        archivo.write("INFORME DE CANDIDATOS\n")
        archivo.write("---------------------\n\n")
        for candidato in candidatos:
            archivo.write("id: " + str(candidato["id"]) + "\n")
            archivo.write("Nombre: " + candidato["nombre"] + " " + candidato["apellidos"] + "\n")
            archivo.write("Puesto: " + candidato["puesto"] + "\n")
            archivo.write("Tecnologia: " + candidato["tecnologia"] + "\n")
            archivo.write("Experiencia: " + str(candidato["experiencia"]) + " años\n")
            archivo.write("Correo: " + candidato["correo"] + "\n")
            archivo.write("Telefono: " + str(candidato["telefono"]) + "\n")
            archivo.write("\n")
        archivo.write("Total de candidatos: " + str(len(candidatos)) + "\n")

# Menú principal que se repite hasta que decides salir
while True:
    print("1. Ver todos los candidatos. \n" \
    "2. Buscar por tecnologia. \n" \
    "3. Agregar candidato. \n" \
    "4. Eliminar candidato. \n" \
    "5. Exportar informe .txt\n" \
    "6. Ver tecnologias disponibles\n" \
    "7. Ver candidatos por puesto\n" \
    "8. Salir")

    opcion_menu=input("Elige una opcion: ")

    if opcion_menu=="1":
        mostrar_candidatos(candidatos)

    elif opcion_menu=="2":
        tecnologia_buscada=input("¿Que tecnologia buscas? ")
        resultado=buscar_tecnologia(tecnologia_buscada)
        if len(resultado)==0:
            print("No se han encontrado candidatos.")
        else:
            mostrar_candidatos(resultado, "Resultados de la busqueda")
        faltan = tecnologias_sin_candidatos(tecnologia_buscada)
        if len(faltan)>0:
            print("Ningun candidato domina:", faltan)

    elif opcion_menu=="3":
        agregar_candidatos()
        print("Candidato agregado correctamente.")

    elif opcion_menu=="4":
        candidato_eliminado=input("Inserta el id del candidato que quieres eliminar: ")
        if candidato_eliminado.isdigit():
            eliminar_candidato(int(candidato_eliminado))
        else:
            print("El id tiene que ser un numero.")

    elif opcion_menu=="5":
        exportar_informe()
        print("Informe guardado correctamente.")

    elif opcion_menu=="6":
        print("Tecnologias disponibles:",listar_tecnologias())

    elif opcion_menu=="7":
        for puesto, cantidad in contar_por_puesto().items():
            print(puesto, ":", cantidad)

    elif opcion_menu=="8":
        print("Cerrando programa...")
        guardar_datos()
        break

    else:
        print("Error. Lo que has introducido no es correcto.")