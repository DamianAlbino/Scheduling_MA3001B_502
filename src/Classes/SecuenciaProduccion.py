import pandas as pd

class SecuenciaProduccion:
    data = pd.DataFrame(columns=['ID_Secuencia', 'ID_Demanda', 'Producto', 'ID_Máquina', 'FechaHoraInicio', 'FechaHoraFin', 'CantidadProgramada', 'UnidadVentas'])
    id_actual = 0

    @classmethod
    def agregar(cls, id_demanda, producto, id_maquina, fecha_hora_inicio, fecha_hora_fin, cantidad_programada, unidad_ventas):
        cls.id_actual += 1
        nuevo_registro = pd.DataFrame.from_dict({
            'ID_Secuencia': [cls.id_actual],
            'ID_Demanda': [id_demanda],
            'Producto': [producto],
            'ID_Máquina': [id_maquina],
            'FechaHoraInicio': [fecha_hora_inicio],
            'FechaHoraFin': [fecha_hora_fin],
            'CantidadProgramada': [cantidad_programada],
            'UnidadVentas': [unidad_ventas]
        })
        cls.data = pd.concat([cls.data, nuevo_registro], ignore_index=True)

    @classmethod
    def eliminar(cls, id_secuencia):
        cls.data = cls.data[cls.data['ID_Secuencia'] != id_secuencia]

    @classmethod
    def mostrar(cls):
        return cls.data

    @classmethod
    def obtener_tiempo_fin(cls, producto, tipo_maquina):
        secuencias_filtradas = cls.data[(cls.data['Producto'] == producto) & (cls.data['ID_Máquina'] == tipo_maquina)]
        if not secuencias_filtradas.empty:
            return secuencias_filtradas['FechaHoraFin'].max()
        return None
