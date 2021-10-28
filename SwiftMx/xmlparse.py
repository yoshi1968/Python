import xml.etree.ElementTree as ET
#xmlデータを読み込みます
tree = ET.parse('country.xml')
#一番上の階層の要素を取り出します
root = tree.getroot()