class Persona:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

class Estudiante(Persona):
    def __init__(self, nombre, genero, examenes):
        super().__init__(nombre, genero)
        self.examenes = examenes


    def contarRegulares(self):
        cantidad = 0
        for e in self.examenes:
            if 2.5 < e['nota'] <= 3.5:
                cantidad += 1
        return cantidad

nombres = {1: "armando", 2: "nicolas", 3: "daniel", 4: "maria", 5: "marcela", 6: "alexandra"}
materias = {1: "quimica", 2: "idiomas", 3: "historia"}

# Datos [estudiante_id, genero_id, materia_id, nota]
datos = [
    [1.0, 0.0, 1.0, 1.1], [1.0, 0.0, 2.0, 1.8], [1.0, 0.0, 3.0, 3.3],
    [2.0, 0.0, 1.0, 4.3], [2.0, 0.0, 2.0, 1.6], [2.0, 0.0, 3.0, 4.3],
    [3.0, 0.0, 1.0, 3.8], [3.0, 0.0, 2.0, 0.7], [3.0, 0.0, 3.0, 1.8],
    [4.0, 1.0, 1.0, 0.6], [4.0, 1.0, 2.0, 2.5], [4.0, 1.0, 3.0, 4.0],
    [5.0, 1.0, 1.0, 0.5], [5.0, 1.0, 2.0, 3.8], [5.0, 1.0, 3.0, 1.2],
    [6.0, 1.0, 1.0, 2.6], [6.0, 1.0, 2.0, 4.6], [6.0, 1.0, 3.0, 0.1]
]

# Crear lista de objetos Estudiante agrupando sus exámenes
estudiantes_dict = {}
for id_est, gen, mat, nota in datos:
    id_est = int(id_est)
    if id_est not in estudiantes_dict:
        estudiantes_dict[id_est] = Estudiante(nombres[id_est], int(gen), [])
    estudiantes_dict[id_est].examenes.append({'materia': int(mat), 'nota': nota})

lista_estudiantes = list(estudiantes_dict.values())
todos_los_examenes = [e for est in lista_estudiantes for e in est.examenes]


# 1. Exámenes con nota mayor al promedio.
promedio = sum(e['nota'] for e in todos_los_examenes) / len(todos_los_examenes)
mayores_promedio = sum(1 for e in todos_los_examenes if e['nota'] > promedio)


# 2. Total de exámenes con calificación Regular usando el método de la clase Estudiante
total_regulares = sum(est.contarRegulares() for est in lista_estudiantes)


# 3. Materia con mayor número de exámenes reprobados (nota <= 2.5)
reprobados_por_materia = {}
for e in todos_los_examenes:
    if e['nota'] <= 2.5:
        reprobados_por_materia[e['materia']] = reprobados_por_materia.get(e['materia'], 0) + 1
        id_materia_mas_reprobada= max(reprobados_por_materia, key = reprobados_por_materia.get)
        materia_mas_reprobada = materias[id_materia_mas_reprobada]


# 4. Estudiante con mejor desempeño en Química (materia ID = 1)
mejor_nota_quimica = -1
estudiante_mejor_quimica = ""

for est in lista_estudiantes:
    for e in est.examenes:
        if e['materia'] == 1 and e['nota'] > mejor_nota_quimica:
            mejor_nota_quimica = e['nota']
            estudiante_mejor_quimica = est.nombre



print(mayores_promedio)
print(total_regulares)
print(materia_mas_reprobada)
print(estudiante_mejor_quimica)
