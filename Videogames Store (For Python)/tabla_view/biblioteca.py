from db_sql.biblioteca import BibliotecaDb
from db_sql.videoJuego import VideoJuego
bib = BibliotecaDb()
video = VideoJuego()



class Biblioteca():
    def __init__(self):
        super().__init__()

    def crearBiblioteca(self, idUsuario):
        video.verNombreVideoJuegos()
        opcion = input("seleccione el juego que quiere: ")
        idVideoJuego = bib.seleccionarIdVideoJuego(opcion)
        while idVideoJuego is None:
            opcion = input("Error, seleccione un juego que si este en la base de datos: ")
            idVideoJuego = bib.seleccionarIdVideoJuego(opcion) 
        bib.crearBiblioteca(idVideoJuego, idUsuario, "actualizado")
    
    


    