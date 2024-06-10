from datetime import timedelta, datetime
from Classes.Maquina import Maquina
from Classes.SecuenciaProduccion import SecuenciaProduccion
from Classes.Demanda import Demanda

def programar_manual(id_maquina, id_demanda, fecha_hora_inicio, unidad_ventas):
    maquinas = Maquina.mostrar()
    demandas = Demanda.mostrar()
    demanda_filtrada = demandas[demandas['ID_Demanda'] == id_demanda]
    maquina_filtrada = maquinas[maquinas['ID_Máquina'] == id_maquina]

    if (not maquina_filtrada.empty) & (not demanda_filtrada.empty):
        producto = demanda_filtrada.iloc[0]['Producto']
        cantidad_requerida = demanda_filtrada.iloc[0]['Cantidad']
        cantidad_programada = demanda_filtrada.iloc[0]['CantidadProgramada']
        capacidad_maquina = maquina_filtrada.iloc[0]['Capacidad']
        capacidad_ocupada = maquina_filtrada.iloc[0]['CapacidadOcupada']

        cantidad_disponible = min(capacidad_maquina - capacidad_ocupada, cantidad_requerida - cantidad_programada)
        if cantidad_disponible > 0:
            duracion_produccion = timedelta(hours=1)  # Asumimos una duración fija de 1 hora por ahora
            fecha_hora_inicio_dt = datetime.strptime(fecha_hora_inicio, '%Y-%m-%d %H:%M:%S')
            fecha_hora_fin = fecha_hora_inicio_dt + duracion_produccion
            
            if maquina_filtrada.iloc[0]['Tipo_Máquina'] == 'Amasadora':
                SecuenciaProduccion.agregar(id_demanda, producto, id_maquina, fecha_hora_inicio_dt, fecha_hora_fin, cantidad_disponible, unidad_ventas)
                Demanda.actualizar_cantidad_programada(id_demanda, cantidad_disponible)
                Maquina.actualizar_capacidad_ocupada(id_maquina, cantidad_disponible)
            elif maquina_filtrada.iloc[0]['Tipo_Máquina'] == 'Horno':
                previous_task_end_time = SecuenciaProduccion.obtener_tiempo_fin(producto, 'Amasadora')
                if fecha_hora_inicio_dt >= previous_task_end_time:
                    SecuenciaProduccion.agregar(id_demanda, producto, id_maquina, fecha_hora_inicio_dt, fecha_hora_fin, cantidad_disponible, unidad_ventas)
                    Demanda.actualizar_cantidad_programada(id_demanda, cantidad_disponible)
                    Maquina.actualizar_capacidad_ocupada(id_maquina, cantidad_disponible)
            elif maquina_filtrada.iloc[0]['Tipo_Máquina'] == 'Empaquetadora':
                previous_task_end_time = SecuenciaProduccion.obtener_tiempo_fin(producto, 'Horno')
                if fecha_hora_inicio_dt >= previous_task_end_time:
                    SecuenciaProduccion.agregar(id_demanda, producto, id_maquina, fecha_hora_inicio_dt, fecha_hora_fin, cantidad_disponible, unidad_ventas)
                    Demanda.actualizar_cantidad_programada(id_demanda, cantidad_disponible)
                    Maquina.actualizar_capacidad_ocupada(id_maquina, cantidad_disponible)

            return True, cantidad_disponible
        else:
            return False, 0
    return False, 0

