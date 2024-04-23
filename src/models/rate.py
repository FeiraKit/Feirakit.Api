from flask_restx import fields
from src.program.server import server
from src.models.id import id
from src.models.configs import avaliacao

request = server.api.model('Rate',  {
    'comentario': fields.String(required=True, description='comentario produto'),
    'nota': fields.Integer(required=True,description='nota'),
    'data': fields.Date(required=True, description='data de envio'),
    'id_cliente': fields.String(required=True, description='id do cliente'),
    'idproduct': fields.String(required=True, description='id do produto')
})
update_request = server.api.model('update_request',  {
    'comentario': fields.String(required=True, description='comentario produto'),
    'nota': fields.Integer(required=True,enum=avaliacao, description='nota')
})

rate_request = server.api.model('RateRequest', id,  {
    'resultado': fields.Nested(request),

})
rate_response = server.api.inherit('RateResponse', request, id)

rate_default_response = server.api.model('RateResponseDefault',  {
    'resultado': fields.Boolean(),
    'mensagem': fields.String(),
})

rate_update_request = server.api.inherit('RateUpdateRequest',  update_request, id)

rate_update_response = server.api.inherit('RateUpdateResponse',  {
    'resultado': fields.Nested(rate_update_request),
    'mensagem': fields.String()
})

rate_average_request = server.api.inherit('RateAverageRequest',  {
    'productid': fields.String(),
})

rate_average_response = server.api.inherit('RateAverageResponse',  {
    'average': fields.Float(),
})