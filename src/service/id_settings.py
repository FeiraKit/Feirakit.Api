from bson import json_util
import json

class IdSettings():
    def get_id(self, entity):
        new_entity = json.loads(json_util.dumps(entity))
        return new_entity['_id']['$oid']
    
    def entity_response_list(self, entities):
        new_entities = []
        for entity in entities:
            entity['id'] = self.get_id(entity)
            new_entities.append(entity)
        return new_entities
    
    def entity_response(self, entity):
        entity['id'] = self.get_id(entity)
        return entity
