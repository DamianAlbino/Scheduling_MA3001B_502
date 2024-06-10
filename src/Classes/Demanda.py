import pandas as pd

class Demanda:
    data = pd.DataFrame(columns=['ID_Demanda', 'Producto', 'Cantidad', 'CantidadProgramada', 'FechaSolicitud', 'Estado'])
    id_actual = 0

    @classmethod
    def agregar(cls, producto, cantidad, FechaSolicitud):
        # assert estado in ['Pendiente', 'En proceso', 'Completada'], "Las demandas solo pueden tener status 'Pendiente', 'En proceso' o 'Completada'."
        cls.id_actual += 1
        nuevo_registro = pd.DataFrame.from_dict({
            'ID_Demanda': [cls.id_actual],
            'Producto': [producto],
            'Cantidad': [cantidad],
            'CantidadProgramada': [0],
            'FechaSolicitud': [FechaSolicitud],
            'Estado': ['Pendiente']
        })
        cls.data = pd.concat([cls.data, nuevo_registro], ignore_index=True)

    @classmethod
    def actualizar_cantidad_programada(cls, id_demanda, cantidad_programada):
        indice = cls.data[cls.data['ID_Demanda'] == id_demanda].index
        if not indice.empty:
            cls.data.at[indice[0], 'CantidadProgramada'] += cantidad_programada
            if cls.data.at[indice[0], 'CantidadProgramada'] == cls.data.at[indice[0], 'Cantidad']:
                cls.data.at[indice[0], 'Estado'] = 'Completada'
            elif cls.data.at[indice[0], 'CantidadProgramada'] > 0:
                cls.data.at[indice[0], 'Estado'] = 'En proceso'
            else:
                cls.data.at[indice[0], 'Estado'] = 'Pendiente'

    @classmethod
    def mostrar(cls):
        return cls.data
