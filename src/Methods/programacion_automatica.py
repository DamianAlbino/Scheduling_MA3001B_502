from datetime import datetime, timedelta
from Classes.Maquina import Maquina
from Classes.Demanda import Demanda
from Classes.SecuenciaProduccion import SecuenciaProduccion
from Classes.Setup import Setup

def programacion_automatica():
    demandas_pendientes = Demanda.data[Demanda.data['Estado'] == 'Pendiente'].sort_values(by=['FechaSolicitud', 'Cantidad'], ascending=[True, False])
    for _, demanda in demandas_pendientes.iterrows():
        producto, cantidad_requerida, fecha_solicitud, id_demanda = demanda['Producto'], demanda['Cantidad'], datetime.fromisoformat(demanda['FechaSolicitud']), demanda['ID_Demanda']
        maquinas_amasado = Maquina.data[(Maquina.data['Tipo_Máquina'] == 'Amasadora') & (Maquina.data['Disponibilidad'] == 'Disponible')].sort_values(by=['Capacidad'], ascending=False)
        for _, maquina in maquinas_amasado.iterrows():
            id_maquina, capacidad_maquina, capacidad_ocupada = maquina['ID_Máquina'], maquina['Capacidad'], maquina['CapacidadOcupada']
            capacidad_disponible = capacidad_maquina - capacidad_ocupada
            if cantidad_requerida <= capacidad_disponible:
                fecha_hora_fin = fecha_solicitud + timedelta(hours=1)
                SecuenciaProduccion.agregar(id_demanda=id_demanda, producto=producto, id_maquina=id_maquina, fecha_hora_inicio=fecha_solicitud, fecha_hora_fin=fecha_hora_fin, cantidad_programada=cantidad_requerida, unidad_ventas="Piezas")
                Maquina.actualizar_capacidad_ocupada(id_maquina, capacidad_ocupada + cantidad_requerida)
                Demanda.actualizar_cantidad_programada(id_demanda, cantidad_requerida)
                break
            else:
                fecha_hora_fin = fecha_solicitud + timedelta(hours=1)
                SecuenciaProduccion.agregar(id_demanda=id_demanda, producto=producto, id_maquina=id_maquina, fecha_hora_inicio=fecha_solicitud, fecha_hora_fin=fecha_hora_fin, cantidad_programada=capacidad_disponible, unidad_ventas="Piezas")
                Maquina.actualizar_capacidad_ocupada(id_maquina, capacidad_maquina)
                Demanda.actualizar_cantidad_programada(id_demanda, capacidad_disponible)
                cantidad_requerida -= capacidad_disponible
        fecha_hora_inicio_horneado = fecha_hora_fin + Setup.data[Setup.data['Descripcion'] == 'Reposo']['Tiempo'].iloc[0]
        maquinas_horneado = Maquina.data[(Maquina.data['Tipo_Máquina'] == 'Horno') & (Maquina.data['Disponibilidad'] == 'Disponible')].sort_values(by=['Capacidad'], ascending=False)
        for _, maquina in maquinas_horneado.iterrows():
            id_maquina, capacidad_maquina, capacidad_ocupada = maquina['ID_Máquina'], maquina['Capacidad'], maquina['CapacidadOcupada']
            capacidad_disponible = capacidad_maquina - capacidad_ocupada
            if cantidad_requerida <= capacidad_disponible:
                fecha_hora_fin_horneado = fecha_hora_inicio_horneado + timedelta(hours=1)
                SecuenciaProduccion.agregar(id_demanda=id_demanda, producto=producto, id_maquina=id_maquina, fecha_hora_inicio=fecha_hora_inicio_horneado, fecha_hora_fin=fecha_hora_fin_horneado, cantidad_programada=cantidad_requerida, unidad_ventas="Piezas")
                Maquina.actualizar_capacidad_ocupada(id_maquina, capacidad_ocupada + cantidad_requerida)
                break
            else:
                fecha_hora_fin_horneado = fecha_hora_inicio_horneado + timedelta(hours=1)
                SecuenciaProduccion.agregar(id_demanda=id_demanda, producto=producto, id_maquina=id_maquina, fecha_hora_inicio=fecha_hora_inicio_horneado, fecha_hora_fin=fecha_hora_fin_horneado, cantidad_programada=capacidad_disponible, unidad_ventas="Piezas")
                Maquina.actualizar_capacidad_ocupada(id_maquina, capacidad_maquina)
                cantidad_requerida -= capacidad_disponible
        fecha_hora_inicio_empaquetado = fecha_hora_fin_horneado + Setup.data[Setup.data['Descripcion'] == 'Limpieza']['Tiempo'].iloc[0]
        maquinas_empaquetado = Maquina.data[(Maquina.data['Tipo_Máquina'] == 'Empaquetadora') & (Maquina.data['Disponibilidad'] == 'Disponible')].sort_values(by=['Capacidad'], ascending=False)
        for _, maquina in maquinas_empaquetado.iterrows():
            id_maquina, capacidad_maquina, capacidad_ocupada = maquina['ID_Máquina'], maquina['Capacidad'], maquina['CapacidadOcupada']
            capacidad_disponible = capacidad_maquina - capacidad_ocupada
            if cantidad_requerida <= capacidad_disponible:
                fecha_hora_fin_empaquetado = fecha_hora_inicio_empaquetado + timedelta(hours=1)
                SecuenciaProduccion.agregar(id_demanda=id_demanda, producto=producto, id_maquina=id_maquina, fecha_hora_inicio=fecha_hora_inicio_empaquetado, fecha_hora_fin=fecha_hora_fin_empaquetado, cantidad_programada=cantidad_requerida, unidad_ventas="Piezas")
                Maquina.actualizar_capacidad_ocupada(id_maquina, capacidad_ocupada + cantidad_requerida)
                break
            else:
                fecha_hora_fin_empaquetado = fecha_hora_inicio_empaquetado + timedelta(hours=1)
                SecuenciaProduccion.agregar(id_demanda=id_demanda, producto=producto, id_maquina=id_maquina, fecha_hora_inicio=fecha_hora_inicio_empaquetado, fecha_hora_fin=fecha_hora_fin_empaquetado, cantidad_programada=capacidad_disponible, unidad_ventas="Piezas")
                Maquina.actualizar_capacidad_ocupada(id_maquina, capacidad_maquina)
                cantidad_requerida -= capacidad_disponible
