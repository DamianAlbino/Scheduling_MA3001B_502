import pandas as pd

class Maquina:
    data = pd.DataFrame(columns=['ID_Máquina', 'Tipo_Máquina', 'Capacidad', 'CapacidadOcupada', 'Disponibilidad'])
    id_actual = 0

    @classmethod
    def agregar(cls, tipo, capacidad):
        assert tipo in ['Amasadora', 'Horno', 'Empaquetadora'], "Los tipos de máquina permitidos son 'Amasadora', 'Horno' y 'Empaquetadora'."
        cls.id_actual += 1
        nuevo_registro = pd.DataFrame.from_dict({
            'ID_Máquina': [cls.id_actual],
            'Tipo_Máquina': [tipo],
            'Capacidad': [capacidad],
            'CapacidadOcupada': [0],
            'Disponibilidad': ['Disponible']})
        cls.data = pd.concat([cls.data, nuevo_registro], ignore_index=True)

    @classmethod
    def cambiar_disponibilidad(cls, id_maquina, nueva_disponibilidad):
        if id_maquina in cls.data['ID_Máquina'].values:
            cls.data.loc[cls.data['ID_Máquina'] == id_maquina, 'Disponibilidad'] = nueva_disponibilidad

    @classmethod
    def actualizar_capacidad_ocupada(cls, id_maquina, cantidad):
        if id_maquina in cls.data['ID_Máquina'].values:
            cls.data.loc[cls.data['ID_Máquina'] == id_maquina, 'CapacidadOcupada'] += cantidad
            capacidad_maquina = cls.data.loc[cls.data['ID_Máquina'] == id_maquina, 'Capacidad'].values[0]
            capacidad_ocupada = cls.data.loc[cls.data['ID_Máquina'] == id_maquina, 'CapacidadOcupada'].values[0]
            if capacidad_ocupada >= capacidad_maquina:
                cls.cambiar_disponibilidad(id_maquina, 'No disponible')
            else:
                cls.cambiar_disponibilidad(id_maquina, 'Disponible')

    @classmethod
    def mostrar(cls):
        return cls.data
