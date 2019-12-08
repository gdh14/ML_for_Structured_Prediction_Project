import json

from mlsp_final.loader.pascal_voc_loader import pascalVOCLoader
from mlsp_final.loader.cityscapes_loader import cityscapesLoader

def get_loader(name):
    """get_loader

    :param name:
    """
    return {
        "pascal": pascalVOCLoader,
        "citiscapes": cityscapesLoader,
    }[name]
