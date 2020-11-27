from logic.dx_logic import Logic



class CuentaUsuario(Logic):
    def __init__(self):
        super().__init__()


    def crearCuenta(self, nombre, apellido, correo, usuario, contrasenia):

        database = self.database
        sql = f"""INSERT INTO epicgames.usuario
        (nombre, apellido, correo, usuario, contrasenia) VALUES (
        '{nombre}', '{apellido}', '{correo}', '{usuario}', '{contrasenia}') """

            
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("La cuenta fue creada correctamente")



    def validarCuenta(self, usuario, contrasenia):
        
        database = self.database
        sql = f"""select * from epicgames.usuario where usuario = '{usuario}'
        and contrasenia = '{contrasenia}'"""
            
        record = database.executeQueryRows(sql)

        for row in record:
            if row["id"]:
                print("")
                return (row["id"])
            elif not row["id"]:
                pass

   
