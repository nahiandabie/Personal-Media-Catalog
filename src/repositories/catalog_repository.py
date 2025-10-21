import xml.etree.ElementTree as ET
from src.services.media_factory import MediaFactory

class CatalogRepository:
    def __init__(self, xml_file="data/catalog.xml"):
        self.xml_file = xml_file

    def load_from_xml(self):
        catalog = []
        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        for media_elem in root:
            media_type = media_elem.tag
            details = {child.tag: child.text for child in media_elem}
            media = MediaFactory.create_media(media_type, **details)
            catalog.append(media)
        return catalog

    def save_to_xml(self, catalog):
        root = ET.Element("catalog")
        for media in catalog:
            tag = media.__class__.__name__.lower()
            media_elem = ET.SubElement(root, tag)
            for attr, value in vars(media).items():
                ET.SubElement(media_elem, attr).text = str(value)
        tree = ET.ElementTree(root)
        tree.write(self.xml_file, encoding="utf-8", xml_declaration=True)
