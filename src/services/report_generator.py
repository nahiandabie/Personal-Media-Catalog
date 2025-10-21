from lxml import etree

class ReportGenerator:
    def __init__(self, xml_path="data/catalog.xml"):
        self.xml_path = xml_path

    def generate_report(self, xslt_path, output_html):
        xml_doc = etree.parse(self.xml_path)
        xslt_doc = etree.parse(xslt_path)
        transform = etree.XSLT(xslt_doc)
        result = transform(xml_doc)
        result.write(output_html, pretty_print=True, encoding="UTF-8")
        print(f"✅ Report generated: {output_html}")
