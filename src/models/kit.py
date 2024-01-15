from flask_restx import fields
from src.program.server import server
from src.models.id import id
from src.models import product

info_produto = server.api.model('InfoProduto', {
    'produto':fields.Nested(product.request_product_kit, required=True),
    'quantidade': fields.Integer(required=True)
})

request = server.api.model('Kit',  {
    'nome': fields.String(required=True, min_Length=1, max_Length=200, description='Nome do kit'),
    'descricao': fields.String(required=True, min_Length=1, max_Length=200, description='Descrição do kit'),
    'produtor_id': fields.String(required=True, min_Length=1, max_Length=50, description='Nome produtor'),
    'imagem_url': fields.List(fields.String),
    'preco': fields.Float(description='valor do produto'),
    'produtos':fields.List(fields.Nested(product.request_product_kit), required=True),
    'info_produtos': fields.List(fields.Nested(info_produto), required=True)
})

response = server.api.inherit('KitResponse', request, id)

update_request = server.api.inherit('KitUpdateRequest',  request, id)

update_response = server.api.inherit('KitUpdateResponse',  {
    'resultado': fields.Nested(server.api.inherit('KitResponse', request, id)),
    'mensagem': fields.String()})

response_default = server.api.model('KitResponseDefault',  {
    'resultado': fields.Boolean(),
    'mensagem': fields.String(),
})

