# todo get working
import xml.etree.ElementTree as ET

FILE_PATH = '../SigmaStudio/AMPI_1.xml'

root = ET.parse(FILE_PATH).getroot()


def get_reg(type):
    for module in root.findall('Schematic/IC/Module/CellName'):
        print(module)


if __name__ == '__main__':
    get_reg('foo')
