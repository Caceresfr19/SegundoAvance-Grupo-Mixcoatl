from logic.dx_logic import Logic
from prettytable import PrettyTable


class BibliotecaDb(Logic):
    def __init__(self):
        super().__init__()


    def seleccionarIdVideoJuego(self, nombreVideoJuego):
        database = self.database
        sql = f"""select * from epicgames.videojuego where nombre = '{nombreVideoJuego}'"""
            
        record = database.executeQueryRows(sql)

        for row in record:
            if row["id"]:
                return (row["id"])
            elif not row["id"]:
                return None

    def crearBiblioteca(self, idVideoJuego, idUsuario, estadoJuego):

        database = self.database
        sql = f"""INSERT INTO epicgames.biblioteca
        (id_videojuego, id_usuario, estadoJuego) VALUES (
        {idVideoJuego}, {idUsuario}, '{estadoJuego}') """
 
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("El juego fue comprado correctamente\n")

    def verBibliteca(self, idUsuario):
        database = self.database
        sql = f"select * from epicgames.view_biblioteca where usuarioId = {idUsuario}"
        
        record = database.executeQueryRows(sql) # fetchall
        x = PrettyTable(["nombre", "estado"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for biblioteca in record:
                x.add_row([biblioteca["nombreVideoJuego"], biblioteca["estadoJuego"]])
        print(x)

    def eliminarBiblioteca(self, idVideoJuego):

        database = self.database
        sql = f"""DELETE FROM epicgames.biblioteca WHERE id_videojuego = {idVideoJuego}"""
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("El videoojuego fue eliminado\n")