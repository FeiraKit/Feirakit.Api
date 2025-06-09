from src.core.var_env import var_env
from src.controllers.products import Product
from src.controllers.users import User
from src.controllers.kits import Kit
from src.program.server import server

app = server.app_flask()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=var_env.port,debug=False)