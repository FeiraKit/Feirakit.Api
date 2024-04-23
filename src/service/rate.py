from bson import ObjectId
from src.program.database import database
from src.service.id_settings import IdSettings
from src.service.configs import configs_service

class Rating(IdSettings):
    def __init__(self):
        self.collection = 'rating'

    def get(self, id):
        rates = database.main[self.collection].find({'idproduct': id})
        return self.entity_response_list(rates), 200

    def post(self, rating):     
        if(rating['nota'] <= 0 or rating['nota'] >= 6):
            return {
            'resultado': False,
            'mensagem': "a nota de ser dada com numeros de 1 a 5"
            }, 200
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
    
    def getbyid(self, id):
        rates = database.main[self.collection].find({'_id':  ObjectId(id)})
        return self.entity_response_list(rates)
    

    def average(self, productid):
        rate = database.main[self.collection].find({'idproduct': productid})
        nota = 0
        avaliacoes = 0
        for i in rate:
            avaliacoes += 1
            nota += i['nota'] 
        
        media = nota / avaliacoes
        return {
            'average': media,
        }, 200



rating_service = Rating()
