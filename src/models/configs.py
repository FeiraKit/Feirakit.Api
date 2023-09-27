from flask_restx import fields
from src.program.server import server
from src.models.id import id

types_response = server.api.model('Units', {
    'unidades': fields.List(fields.String),
    'categorias': fields.List(fields.String)
})