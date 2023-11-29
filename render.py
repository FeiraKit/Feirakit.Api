from src.controllers.products import Product, ProductSeachById, ProductSeachByName, ProductSeachByNameOfUsuario
from src.controllers.users import User
from src.controllers.kits import Kit
from src.program.server import server
from src.core.var_env import var_env


app = server.app

if __name__ == '__main__':
    app.run(host='0.0.0.0', 
            port=var_env.port,
            debug=False)