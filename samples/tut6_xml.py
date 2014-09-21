import xml.etree.ElementTree as ET


tree = ET.parse('tut6.xml')
root = tree.getroot()

#xmldata = '<bar><test/></bar>'
#root = ET.fromstring(xmldata)

print root.tag

print root.attrib['name']

child1 = root.find('child1')
print child1.text

for child in root.findall('child1'):
    print child.text