"""
convert user to xml, and load xml to user
"""

import xml.etree.ElementTree as ET 
import xml.dom.minidom as minidom  


def dict_to_xml(input_dict, outpath, root_tag, node_tag):
    root_name = ET.Element(root_tag)
    for item in input_dict:
        node_name = ET.SubElement(root_name, node_tag)
        for key, val in item.items():
            ET.SubElement(node_name, key).text = ', '.join(str(val).split(':'))
    dom = minidom.parseString(ET.tostring(root_name))
    with open(outpath, 'w+') as fs:
        dom.writexml(fs, addindent="    ", newl="\n", encoding="utf-8")


def xml_to_user(in_path):
    # xml to dict
    root = ET.parse(in_path).getroot()
    dict_new = []
    for key, value in enumerate(root):
        dict_init = {}
        for item in value:
            dict_init[item.tag] = item.text
        dict_new.append(dict_init)
    return dict_new