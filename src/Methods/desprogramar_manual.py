from Classes.SecuenciaProduccion import SecuenciaProduccion
from Classes.Demanda import Demanda
from Classes.Maquina import Maquina

def desprogramar_manual(id_maquina, id_demanda, fecha_hora_inicio):
    secuencias = SecuenciaProduccion.mostrar()
    demandas = Demanda.mostrar()
    
    filtro = (secuencias['ID_Máquina'] == id_maquina) & \
             (secuencias['ID_Demanda'] == id_demanda) & \
             (secuencias['FechaHoraInicio'] == fecha_hora_inicio)

    secuencias_filtradas = secuencias[filtro]

    if not secuencias_filtradas.empty:
        for index in secuencias_filtradas.index:
            cantidad_programada = secuencias_filtradas.loc[index]['CantidadProgramada']
            SecuenciaProduccion.eliminar(secuencias_filtradas.loc[index]['ID_Secuencia'])
            

            Demanda.actualizar_cantidad_programada(id_demanda, -cantidad_programada)
            Maquina.actualizar_capacidad_ocupada(id_maquina, -cantidad_programada)

        return True, -cantidad_programada
    else:
        return False, "No se encontró la tarea especificada para desprogramar."
