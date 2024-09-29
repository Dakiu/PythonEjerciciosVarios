from error import LargoExcedidoException
from anuncio import Anuncio, Video, Display, Social

class Campana():
    def __init__(self, nombre: str, fecha_inicio, fecha_termino, anuncios: list):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = self.__obtener_instancia_anuncio(anuncios)

    def __obtener_instancia_anuncio(self, anuncios):
        print(anuncios)
        listaAnuncios = []
        for a in anuncios:
            if a["tipo"] == "video":
                anuncio = Video(a["url_archivo"], a["url_clic"], a["sub_tipo"],a["duracion"])
            if a["tipo"] == "display":
                anuncio = Display(a["ancho"],a["alto"],a["url_archivo"], a["url_clic"], a["sub_tipo"])
            if a["tipo"] == "social":
                anuncio = Social(a["ancho"],a["alto"],a["url_archivo"], a["url_clic"], a["sub_tipo"])
            listaAnuncios.append(anuncio)
        return listaAnuncios         
      
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) > 250:
            raise LargoExcedidoException("Largo Excedido")
        self.__nombre = nombre
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino
    @property
    def anuncios(self):
        return self.__anuncios
    
    def __str__(self):
        cant_video = len(list(filter(lambda x: isinstance(x, Video), self.__anuncios)))
        cant_display = len(list(filter(lambda x: isinstance(x, Display), self.__anuncios)))
        cant_social = len(list(filter(lambda x: isinstance(x, Social), self.__anuncios)))
        return f"Nombre de la Campaña: {self.__nombre}\nAnuncios: {cant_video} Video, {cant_display} Display, {cant_social} Social"
