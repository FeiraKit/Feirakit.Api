from flask_restx import fields
from src.program.server import server

types_response = server.api.model('Units', {
    'unidades': fields.List(fields.String),
    'categorias': fields.List(fields.String)
})

avaliacao = [1, 2, 3, 4, 5]