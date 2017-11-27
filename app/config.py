import os

import yaml

######################################################################
# Paths
######################################################################
PATH_ROOT = os.path.dirname(os.path.abspath(__file__))
PATH_INSTANCE = os.path.join(PATH_ROOT, 'instance')

PATH_SECURE = os.path.join(PATH_INSTANCE, 'secure.yaml')


with open(PATH_SECURE, 'r') as PATH_SECURE_FILE_OBJ:
    SECURE_CONFIG = yaml.load(PATH_SECURE_FILE_OBJ.read())

AWS = SECURE_CONFIG['aws']
