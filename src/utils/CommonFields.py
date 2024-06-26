from enum import Enum

from src.configuration.Configuration import Configuration


class CommonFields(Enum):
    _front_link = Configuration.front_url
    _back_link = Configuration.back_url
    _static_folder = f'{_back_link}/{Configuration.static_folder}/images'
    _contact_mail = Configuration.contact_mail
