def minimizar_latencia(L_deadline, T_tareas):
    tareas_con_deadline = []
    for i in range(len(T_tareas)):
        tareas_con_deadline.append((T_tareas[i], L_deadline[i]))
    tareas_con_deadline.sort(key=lambda x: x[1])  # Ordenar por deadline
    print(tareas_con_deadline)
    latencias = []
    tiempo_inicio = 0
    for tarea in tareas_con_deadline:
        tiempo_fin = tiempo_inicio + tarea[0]
        tiempo_inicio = tiempo_fin
        latencia = tiempo_fin - tarea[1] if tiempo_fin > tarea[1] else 0
        latencias.append((tarea[0], latencia))
    return latencias


if __name__ == "__main__":
    L_deadline = [3, 1, 2]
    T_tareas = [10, 20, 30]
    print(minimizar_latencia(L_deadline, T_tareas))
    L_deadline2 = [10, 20, 30]
    T_tareas2 = [15, 25, 35]
    print(minimizar_latencia(L_deadline2, T_tareas2))
    #[(10, 10), (1, 100)]
    L_deadline3 = [100, 10]
    T_tareas3 = [1, 10]
    print(minimizar_latencia(L_deadline3, T_tareas3))
