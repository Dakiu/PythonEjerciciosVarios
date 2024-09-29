
from ApiService import request_get
from TemplateUtil import CrearTemplate
from HtmlRender import CrearWeb


if __name__ == "__main__":
    aveInfo = request_get("https://aves.ninjas.cl/api/birds")[:6]
    templateHtml = CrearTemplate(aveInfo)
    CrearWeb(templateHtml)

    








