from enum import Enum

from src.configuration.Settings import settings


class CommonFields(Enum):
    _front_link = settings.front_url
    _back_link = settings.back_url
    _static_folder = f'{_back_link}/{settings.static_folder}/images'
    _contact_mail = settings.contact_mail
