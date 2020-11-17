token = '1401455044:AAH55aWHKFJAn1emR_j3o5PIXWbLxAmYe24'

from enum import Enum

db_file = 'database.vdb'


class States(Enum):
    S_START = "0"
    S_ENTER_DAY = "1"
    S_COUNTRY_OR_REGION = "2"
    S_ENTER_COUNTRY_OR_REGION = "3"
    S_ENTER_FIELD_LIST = "4"
