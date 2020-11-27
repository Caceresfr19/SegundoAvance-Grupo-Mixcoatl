from logic.dx_logic import Logic
from prettytable import PrettyTable


class VideoJuego(Logic):
    def __init__(self):
        super().__init__()

    def crearCategoria(self, categoria):

        database = self.database
        sql = f"""INSERT INTO epicgames.categoria
        (categoria) VALUES (
        '{categoria}') """
 
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("La categoria fue creada correctamente")

    def validarCategoria(self, categoria):

        database = self.database
        sql= f"""select * from epicgames.categoria where categoria = '{categoria}' """

        record = database.executeQueryRows(sql)


        if record:
            for row in record:
                if row["id"]:
                    return row["id"]
        else:
            self.crearCategoria(categoria)
            idCategoria = self.validarCategoria(categoria)
            return idCategoria


    def crearVideoJuego(self, nombre, idCategoria, idDesarrollador, descripcion, precio, anio, version):

        database = self.database
        sql = f"""INSERT INTO epicgames.videojuego
        (nombre, id_categoria, id_desarrollador, descripcion, precio, anio, version) VALUES (
        '{nombre}', {idCategoria}, {idDesarrollador}, '{descripcion}', {precio}, {anio}, {version}) """

            
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("El videojuego fue creado correctamente")

    
    def actualizarVideoJuego(self, idVideoJuego, nuevaVersion):

        try:
            database = self.database

            sql = f"""UPDATE epicgames.videojuego SET version = {nuevaVersion} WHERE id = {idVideoJuego}"""
            
            count = database.executeNonQueryRows(sql)

            if count > 0:
                print()
                print("El videojuego se actualizo correctamente\n")

                sql = f"""UPDATE epicgames.biblioteca SET estadoJuego = 'actualizacion pendiente' WHERE id_videojuego = {idVideoJuego};"""
                database.executeNonQueryRows(sql)


        except Exception:
            print()
            print("no se pudo actualizar correctamente")

        finally:
            pass

   

    def verVideoJuegosDesarrollador(self, idDesarrollador):
        database = self.database
        sql = f"select * from epicgames.view_videojuego where idDesarrollador = {idDesarrollador}"

        record = database.executeQueryRows(sql) # fetchall
        x = PrettyTable(["nombre", "categoria", "descripcion", "precio", "año", "version"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for videojuego in record:
                x.add_row([videojuego["nombreVideoJuego"], videojuego["categoria"],videojuego["descripcion"], 
                           videojuego["precio"], videojuego["anio"], videojuego["version"]])
        print(x)
    
    def verNombreVideoJuegos(self):
        database = self.database
        sql = "select * from epicgames.view_videojuego"

        record = database.executeQueryRows(sql) # fetchall
        x = PrettyTable(["nombre"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for biblioteca in record:
                x.add_row([biblioteca["nombreVideoJuego"]])
        print(x)

    
    def seleccionarIdVideoJuego(self, videoJuego):
        
        database = self.database
        sql = f"select * from epicgames.videojuego where nombre = '{videoJuego}'"

        record = database.executeQueryRows(sql)

        if record:   # ve si no da None
            for row in record:    #fetchall
                if row["id"]:
                    return row["id"]
        
        else:
            return None