from bson import ObjectId
from src.program.database import database
from src.service.id_settings import IdSettings
from src.service.configs import configs_service

class Rating(IdSettings):
    def __init__(self):
        self.collection = 'rating'

    def get(self):
        rates = database.main[self.collection].find()
        return self.entity_response_list(rates)

    def post(self, rating):           
        database.main[self.collection].insert_one(rating)
        return {
            'resultado': True,
            'mensagem': "avaliação criada com sucesso"
        }, 201
    
    def put(self, rating):
        my_query = {'_id':  ObjectId(rating['id'])}
        del rating['id']
        new_values = {'$set': rating}
        database.main[self.collection].update_one(my_query, new_values)
        updated_rating = database.main[self.collection].find_one(my_query)
        return {
            'resultado': self.entity_response(updated_rating),
            'mensagem': "O produto foi alterado com sucesso"
        }, 201

    def delete(self, id):
        database.main[self.collection].delete_one({'_id':  ObjectId(id)})
        return {
            'resultado': True,
            'mensagem': "avaliação apagada com sucesso"
        }, 200


rating_service = Rating()
