import pandas as pd

class Setup:
    data = pd.DataFrame(columns=['ID_Setup', 'Descripcion', 'Tiempo'])
    id_actual = 0

    @classmethod
    def agregar(cls, descripcion, tiempo):
        cls.id_actual += 1
        nuevo_registro = pd.DataFrame.from_dict({
            'ID_Setup': [cls.id_actual],
            'Descripcion': [descripcion],
            'Tiempo': [tiempo]})
        cls.data = pd.concat([cls.data, nuevo_registro], ignore_index=True)

    @classmethod
    def eliminar(cls, id_setup):
        cls.data = cls.data[cls.data['ID_Setup'] != id_setup]

    @classmethod
    def mostrar(cls):
        return cls.data
