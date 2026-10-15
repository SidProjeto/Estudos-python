import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class JSON:
    def exportar(self, valor):
        return json.dumps(
            valor,
            default= lambda obj: obj.__dict__,
            indent=4,
            ensure_ascii=False
            )



class XML:
    def exportar(self, valor):
        raiz = ET.Element('dados')
        lista = valor if isinstance(valor, list) else [valor]

        for objeto in lista:
            classe = objeto.__class__.__name__
            tag_item = ET.SubElement(raiz, classe)

            for chave, dvalor in objeto.__dict__.items():
                sub_tag = ET.SubElement(tag_item, chave)
                sub_tag.text = str(dvalor)

        xml = ET.tostring(raiz, encoding='utf-8')
        dom = minidom.parseString(xml)
        xml_organizado = dom.toprettyxml(indent='    ', encoding='utf-8')

        return xml_organizado.decode('utf-8')
                
            


def exportar_dados(metodo, valor):
    print(metodo.exportar(valor))