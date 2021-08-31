from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

def convertJson2Xml(input_file_name,output_file_name):
    data = readfromjson(input_file_name)
    xml = json2xml.Json2xml(data, wrapper="all", pretty=True, attr_type=False).to_xml()
    output_file_name = 'XML_FILES/'+output_file_name
    with open(output_file_name, 'w') as file:
        file.write(str(xml))
    print(output_file_name+" Created")

'''
----------------Second Approach------------------------
import dicttoxml
with open("DEPARTMENT_RESULT.json", "r") as json_file:
    data = json.load(json_file);

    xml = dicttoxml.dicttoxml(data)
    f = open("sample.xml", "w")
    f.write(str(xml))
    print(xml)
'''