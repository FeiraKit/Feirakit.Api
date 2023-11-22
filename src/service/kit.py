from bson import ObjectId
from src.program.database import database
from src.service.id_settings import IdSettings
from src.service.configs import configs_service

class Kit(IdSettings):
    def __init__(self):
        self.collection = 'kit'

    def get(self, page, limit, sort):
        skip = limit * (page - 1)
        kits = list(database.main[self.collection].find().skip(
            skip).limit(limit).sort('_id', sort))
        return self.entity_response_list(kits)

    def post(self, kit, current_user):
        if kit['produtor_id'] != current_user['id']:
            return {
                'resultado': False,
                'mensagem': "erro ao cadastrar kit, os dados de usuário são inconsitentes"
            }, 401
            
        database.main[self.collection].insert_one(kit)
        return {
            'resultado': True,
            'mensagem': "Kit criado com sucesso"
        }, 201
    
    def put(self, kit, current_user):
        if kit['produtor_id'] != current_user['id']:
            return {
                'resultado': {},
                'mensagem': "erro ao atualizar produto,esse produto pertence a outro usuário"
            }, 403

        my_query = {'_id':  ObjectId(kit['id'])}
        del kit['id']
        new_values = {'$set': kit}
        database.main[self.collection].update_one(my_query, new_values)
        updated_product = database.main[self.collection].find_one(my_query)
        return {
            'resultado': self.entity_response(updated_product),
            'mensagem': "O kit foi alterado com sucesso"
        }, 201

    def delete(self, id, current_user):
        kit = database.main[self.collection].find_one({'_id':  ObjectId(id)})
        if kit['produtor_id'] != current_user['id']:
            return {
                'resultado': False,
                'mensagem': "erro ao apagar kit, esse produto pertence a outro usuário"
            }, 403

        database.main[self.collection].delete_one({'_id':  ObjectId(id)})
        return {
            'resultado': True,
            'mensagem': "Kit apagado com sucesso"
        }, 200

    def get_one(self, id):
        kit = database.main[self.collection].find_one({'_id':  ObjectId(id)})
        return self.entity_response(kit)

    def get_kits_by_name(self, name):
        kits = list(database.main[self.collection].find(
            {'nome': {'$regex': name, '$options' : 'i'}}))
        return self.entity_response_list(kits)

    def get_kits_by_id_usuario(self, id_usuario):
        kits = list(database.main[self.collection].find(
            {'produtor_id': id_usuario}))
        return self.entity_response_list(kits)

    def get_kit_types(self):
        kit_types = configs_service.get()
        return kit_types

kit_service = Kit()
