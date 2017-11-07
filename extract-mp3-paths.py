import sys
import xml.etree.ElementTree as ET
import urllib.request
tree = ET.ElementTree(file=urllib.request.urlopen(sys.argv[1]))
root = tree.getroot()
for lilnode in root.findall('./channel/item/enclosure'):
#'./channel/{http://ww.itunes.cm/dtds/podcast-1.0.dtd}'):
    print(lilnode.attrib['url'])
