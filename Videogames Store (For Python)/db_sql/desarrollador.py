from logic.dx_logic import Logic



class CuentaDesarrollador(Logic):
    def __init__(self):
        super().__init__()


    def crearCuenta(self, nombre, apellido, usuario, contrasenia):

        database = self.database
        sql = f"""INSERT INTO epicgames.desarrollador
        (nombre, apellido, usuario, contrasenia) VALUES (
        '{nombre}', '{apellido}', '{usuario}', '{contrasenia}') """

            
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("La cuenta fue creada correctamente")



    def validarCuenta(self, usuario, contrasenia):
        
        database = self.database
        sql = f"""select * from epicgames.desarrollador where usuario = '{usuario}'
        and contrasenia = '{contrasenia}'"""
            
        record = database.executeQueryRows(sql)

        for row in record:
            if row["id"]:
                print("")
                return (row["id"])
            elif not row["id"]:
                pass

   