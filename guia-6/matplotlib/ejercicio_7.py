import pandas as pd
import matplotlib.pyplot as plt

url_sheet = "https://docs.google.com/spreadsheets/d/17ei_NER5i_R-9QLnkeIjNprzTyoSqGowJ8yrT9tbi_8/export?format=csv"
df = pd.read_csv(url_sheet)

fig, ax = plt.subplots()

## Punto A
# alumnos_presentes = df[df['Nota 1° Parcial'].notnull()]
# alumnos_ausentes = df[df['Nota 1° Parcial'].isnull()].fillna(0)
# labels = ['Presentes', 'Ausentes']
# ax.pie([alumnos_presentes.shape[0], alumnos_ausentes.shape[0]], labels=labels, autopct='%1.1f%%')
# ax.set_title('Porcentaje de asistencias en el parcial')
# plt.show()

## Punto B
# alumnos_presentes = df[df['Nota 1° Parcial'].notnull()]
# aprobados = alumnos_presentes[alumnos_presentes['Nota 1° Parcial'] >= 4]['Nota 1° Parcial'].shape[0]
# desaprobados = alumnos_presentes[alumnos_presentes['Nota 1° Parcial'] < 4]['Nota 1° Parcial'].shape[0]
# labels = ['Aprobados', 'Desaprobados']
# ax.bar(labels, [aprobados, desaprobados])
# ax.set_title('Aprobados y Desaprobados en el 1° Parcial')
# ax.set_ylabel('Cantidad de Alumnos')
# ax.set_xlabel('Estado del Alumno')
# plt.show()

## Punto D

def promedio_curso(df):
    aprobados = df[df['Nota 1° Parcial'] >= 4]
    ultimo_curso = df.tail(1)['Curso']
    promedios = []
    cursos = []

    for i in range(1, int(ultimo_curso.iloc[0]) + 1):
        if (i == 5):
            curso = "05 o 06"
        elif (i == 6):
            continue
        else:
            curso = f"0{i}" if i < 10 else str(i)

        promedio = aprobados[aprobados['Curso'] == curso]['Nota 1° Parcial'].mean()
        promedios.append(promedio)
        cursos.append(curso)

    return cursos, promedios
    
x, y = promedio_curso(df)
print(y)
ax.plot(x, y, label='Aprobados')
ax.set_title('Promedio de aprobados')
ax.set_xlabel('Cursos')
ax.set_ylabel('Promedio')
ax.legend()
ax.grid()
plt.show()

## Punto C
# y = df['Nota 1° Parcial']
# x = df['Curso']
# ax.scatter(x, y)
# ax.set_title('Relacion entre curso y nota individual')
# ax.set_xlabel('Cursos')
# ax.set_ylabel('Nota')
# plt.show()