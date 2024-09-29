from abc import abstractmethod, ABC
from error import SubTipoInvalidoException

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.__ancho = ancho
        self.__alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho):
        if ancho < 0:
            self.ancho = 1
        else:
            self.__ancho = ancho
    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self, alto):
        if alto < 0:
            self.alto = 1
        else:
            self.__alto = alto
    @property
    def url_archivo(self):
        return self.__url_archivo
    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo
    @property
    def url_clic(self):
        return self.__url_clic
    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS or isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS or isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS:
            raise SubTipoInvalidoException("subtipo inválido")
        else:
            self.__sub_tipo = sub_tipo
    @staticmethod
    def mostrar_formatos():
        print("FORMATO VIDEO:")
        print("==============")
        for v in Video.SUB_TIPOS:
            print(f"- {v}")
        print("FORMATO DISPLAY:")
        print("==============")
        for d in Display.SUB_TIPOS:
            print(f"- {d}")
        print("FORMATO SOCIAL:")
        print("==============")
        for s in Social.SUB_TIPOS:
            print(f"- {s}")
    @abstractmethod
    def redimensionar_anuncio(self):
        pass
    @abstractmethod
    def comprimir_anuncio(self):
        pass
    
class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5 
    @property
    def duracion(self):
        return self.__duracion
    @duracion.setter
    def duracion(self, duracion):
        if duracion < 0:
            self.__duracion = 5
        else:
            self.__duracion = duracion
    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho):
        if ancho < 0:
            self.ancho = 1
        else:
            self.__ancho = ancho
    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self, alto):
        if alto < 0:
            self.alto = 1
        else:
            self.__alto = alto

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS or isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS or isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS:
            raise SubTipoInvalidoException("subtipo inválido")
        else:
            self.__sub_tipo = sub_tipo
    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio():
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def __init__(self, ancho, alto, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio():
        print( "REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")