def dhondt(votos,bancas_totales):
    cantidad_de_agrupaciones = len(votos)
    bancas_por_agrupacion = [0]*cantidad_de_agrupaciones
    while sum(bancas_por_agrupacion)<bancas_totales:
        cocientes = [0]*cantidad_de_agrupaciones
        for i in range(cantidad_de_agrupaciones):
            cocientes[i] = votos[i] / (bancas_por_agrupacion[i] + 1)
        ind_cociente_max = 0
        for i in range(cantidad_de_agrupaciones):
            if(cocientes[i] > cocientes[ind_cociente_max]):
                ind_cociente_max = i
        bancas_por_agrupacion[ind_cociente_max] += 1
    return bancas_por_agrupacion

def bancas_por_agrupacion(votos,bancas_totales,padron):
    votos_mayores_al_3 = []
    for agrupacion in votos:
        if agrupacion/padron >= 0.03:
            votos_mayores_al_3.append(agrupacion)
    return dhondt(votos_mayores_al_3,bancas_totales)