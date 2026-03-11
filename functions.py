def promedio_estudiantes(calificaciones):
    if len(calificaciones) == 0:
        return 0
    promedio = sum(calificaciones) / len(calificaciones)
    return float(promedio)
calificaciones = [85, 92 ,78]
print(promedio_estudiantes(calificaciones))