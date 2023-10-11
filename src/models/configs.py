from flask_restx import fields
from src.program.server import server

types_response = server.api.model('Units', {
    'unidades': fields.List(fields.String),
    'categorias': fields.List(fields.String)
})