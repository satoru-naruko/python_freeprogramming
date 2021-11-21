"""
<?xml version=1.0 encoding='utf-8 ?>
<root>
    <employee>
        <employ>
            <id>111</id>
            <name>satoru</name>
        </employ>
        <employ>
            <id>222</id>
            <name>tarou</name>
        </employ>
    </employee>
</root>
"""
import xml.etree.ElementTree as ET

root = ET.Element('root')
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, 'employee')

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '111'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = "satoru"

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '222'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = "tarou"

tree.write('test.xml', encoding='utf-8', xml_declaration=True)

