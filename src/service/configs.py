from src.config.database import database
from src.service.id_settings import IdSettings

class Configs(IdSettings):
    def __init__(self):
        self.collection = 'configs'

    def get(self):
        configs = database.main[self.collection].find_one()
        return {
            'unidades': configs['Unites'],
            'categorias': configs['Categories']
        }, 200

configs_service = Configs()
