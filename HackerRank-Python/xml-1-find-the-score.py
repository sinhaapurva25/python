import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    for i in node: print(i)
    return 0

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(root)
    print(get_attr_number(root))