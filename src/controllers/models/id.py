from flask_restx import fields
from src.config.server import server

id =  {
    'id': fields.String(description='ID do registro', required=True),
}

id_request = server.api.model('Id', id )
