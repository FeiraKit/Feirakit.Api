from flask_restx import fields
from src.program.server import server
from src.models.id import id

address = server.api.model('Address', {
    'rua': fields.String(required=True, min_Length=3, max_Length=200, description='Rua'),
    'numero': fields.String(required=True, min_Length=1, max_Length=1000, description='Numero'),
    'bairro': fields.String(required=True, min_Length=3, max_Length=200, description='Bairro'),
    'cep': fields.String(required=True, min_Length=8, max_Length=8, description='CEP'),
    'complemento': fields.String(required=True, min_Length=3, max_Length=200, description='Complemento'),
    'cidade': fields.String(required=True, min_Length=3, max_Length=200, description='Cidade'),
    'estado': fields.String(required=True, min_Length=1, max_Length=3, description='estado'),
})

base_user = server.api.model('User', {
    'nome': fields.String(required=True, min_Length=3, max_Length=200, description='Nome completo do usuário'),
    'email': fields.String(required=True, min_Length=5, max_Length=200, description='Email'),
    'telefone': fields.String(required=True, min_Length=6, max_Length=20, description='Telefone'),
    'endereco': fields.Nested(address)
})

request = server.api.model('UserRequest',  {
    'nome': fields.String(required=True, min_Length=3, max_Length=200, description='Nome completo do usuário'),
    'email': fields.String(required=True, min_Length=5, max_Length=200, description='Email'),
    'telefone': fields.String(required=True, min_Length=6, max_Length=20, description='Telefone'),
    'senha': fields.String(required=True, min_Length=4, max_Length=200, description='Senha'),
    'endereco': fields.Nested(address)
})

response = server.api.model('UserResponse',  {
    'resultado': fields.List(fields.Nested(server.api.inherit('userResponse',  base_user, id))),
    'mensagem': fields.String(),
})

updated_response = server.api.model('UserResponse',  {
    'resultado': fields.Nested(server.api.inherit('userResponse',  base_user, id)),
    'mensagem': fields.String(),
})

create_response = server.api.model('UserCreateResponse',  {
    'resultado': fields.Boolean(),
    'mensagem': fields.String(),
})

update_request = server.api.inherit('userUpdateRequest',  server.api.model('userUpdateRequestProps',  {
    'nome': fields.String(required=True, min_Length=3, max_Length=200, description='Nome completo do usuário'),
    'email': fields.String(required=True, min_Length=5, max_Length=200, description='Email'),
    'telefone': fields.String(required=True, min_Length=6, max_Length=20, description='Telefone'),
    'endereco': fields.Nested(address)
}), id)

check_password_request = server.api.model('checkPasswordRequest',  {
    'email': fields.String(required=True, min_Length=5, max_Length=200, description='Email'),
    'senha': fields.String(required=True, min_Length=4, max_Length=200, description='Senha a ser verificada'),
})

change_password_request = server.api.model('changePasswordRequest',  {
    'email': fields.String(required=True, min_Length=5, max_Length=200, description='Email'),
    'senha': fields.String(required=True, min_Length=4, max_Length=200, description='Senha antiga'),
    'nova_senha': fields.String(required=True, min_Length=4, max_Length=200, description='Nova senha'),
})

response_default = server.api.model('responseDefault',  {
    'resultado': fields.Boolean(),
    'mensagem': fields.String(),
})

response_login_default = server.api.model('responseLoginDefault',  {
    'resultado': fields.Boolean(),
    'token': fields.String(),
    'mensagem': fields.String(),
})
