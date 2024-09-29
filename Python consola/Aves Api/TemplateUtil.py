from string import Template

def CrearTemplate(aveInfo):

    html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Aves de Chile</title>
                            </head>
                         
                            <body>
                                    <br>
                                <table width=100%>
                                    <tr>
                                        <th width='40%'><center><h4>Imagen</h4></center></th>
                                        <th width='30%'><center><h4>Nombre</h4></center></th>
                                        <th width='30%'><center><h4>Name</h4></center></th>
                                    </tr>
                                    <tr>
                                        <td width='40%'><center><img src=$url></center></td>
                                        <td width='30%'><center>$nomEspanol</center></td>
                                        <td width='30%'><center> $nomEnglish</center></td>
                                    <tr>
                                </table>
                            </body>
                            </html>
                        ''')
    texto_img = ''

    for ave in aveInfo:
        img = ave["images"]["main"]
        texto_img += html_template.substitute(url = img, nomEspanol = ave["name"]["spanish"], nomEnglish = ave["name"]["english"])

    return texto_img