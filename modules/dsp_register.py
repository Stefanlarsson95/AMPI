# todo get working
import xml.etree.ElementTree as ET
import time

FILE_PATH = '../SigmaStudio/AMPI_1.xml'

root = ET.parse(FILE_PATH).getroot()

def get_reg(conf_dict):
    for module in root.findall('IC/'):
        if module.tag != 'Module':
            continue
        name = -1
        for cell in module:
            _name = cell.text
            if '\n' not in _name:
                name = _name
                #time.sleep(0.1)
            for alg in cell:
                if alg.tag != 'ModuleParameter':
                    continue
                for param in alg:
                    if param.tag != 'Data' or conf_dict.get(name) is not None:
                        continue
                    conf_dict[name] = 0
                    for data in param.text.split(', '):
                        if data == '':
                            continue
                        d = int(data, 16)


                        conf_dict[name] = (conf_dict[name] << 8) + d


if __name__ == '__main__':
    conf_dict = {}
    get_reg(conf_dict)
    for reg in conf_dict:
        print(reg + ': ' + hex(conf_dict.get(reg)) + '\n')
