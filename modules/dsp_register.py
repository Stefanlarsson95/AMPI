# todo get working
import xml.etree.ElementTree as ET
import time

FILE_PATH = '../SigmaStudio/AMPI_1.xml'


def get_reg(xml_path=FILE_PATH):
    root = ET.parse(xml_path).getroot()

    _conf_dict = {}

    for module in root.findall('IC/'):
        if module.tag != 'Module':
            continue
        name = -1
        for cell in module:
            _name = cell.text
            if '\n' not in _name:
                name = _name
                time.sleep(0.05)
            for alg in cell:
                if alg.tag != 'ModuleParameter':
                    continue
                for param in alg:
                    if param.tag != 'Data' or _conf_dict.get(name) is not None:
                        continue
                    _conf_dict[name] = 0
                    for data in param.text.split(', '):
                        if data == '':
                            continue
                        d = int(data, 16)

                        _conf_dict[name] = (_conf_dict[name] << 8) + d

    return _conf_dict


if __name__ == '__main__':
    conf_dict = get_reg()
    for reg in conf_dict:
        print(reg + ': ' + hex(conf_dict.get(reg)) + '\n')
