import json

from ptsemseg.loader.pascal_voc_loader import pascalVOCLoader

def get_loader(name):
    """get_loader

    :param name:
    """
    return {
        "pascal": pascalVOCLoader,
    }[name]
