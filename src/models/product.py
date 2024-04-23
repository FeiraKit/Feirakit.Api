from flask_restx import fields
from src.program.server import server
from src.models.id import id

request = server.api.model('Product',  {
    'nome': fields.String(required=True, min_Length=1, max_Length=200, description='Nome do produto'),
    'categoria': fields.String(required=True, description='Tipo de produto'),
    'descricao': fields.String(required=True, min_Length=1, max_Length=200, description='Descrição do produto'),
    'unidade': fields.String(required=True, description='Unidade do produto'),
    'estoque': fields.Integer(required=True, description='Quantidade no estoque'),
    'produtor_id': fields.String(required=True, min_Length=1, max_Length=50, description='id produtor'),
    'cidades': fields.List(fields.String,required=True, description='cidades que o produto vai estar disponivel'),
    'bestbefore': fields.Boolean(required=True, description='Produto colhido após a compra'),
    'validade': fields.Date(required=True, description='Validade do produto'),
    'imagem_url': fields.List(fields.String),
    'preco': fields.Float(description='valor do produto'),
})

request_product_kit = server.api.inherit('ProductRequestForKit', request, id)

response = server.api.inherit('ProductResponse', request, id)

update_request = server.api.inherit('ProductUpdateRequest',  request, id)

update_response = server.api.inherit('ProductUpdateResponse',  {
    'resultado': fields.Nested(server.api.inherit('ProductResponse', request, id)),
    'mensagem': fields.String()
})

response_default = server.api.model('ProductResponseDefault',  {
    'resultado': fields.Boolean(),
    'mensagem': fields.String(),
})

types_response = server.api.model('Units', {
    'unidades': fields.List(fields.String),
    'categorias': fields.List(fields.String)
})

cities = server.api.model('Cities', {
    'nome': fields.String()
})

cities_response = server.api.model('CitiesResponse',  {
    'resultado': fields.Nested(cities),
    'mensagem': fields.String()
})
