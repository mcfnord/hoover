import xml.etree.ElementTree as ET
tree = ET.parse("my.opml")
root = tree.getroot()
for lilnode in root.findall('./body/outline'):
    print(lilnode.attrib['xmlUrl'])

