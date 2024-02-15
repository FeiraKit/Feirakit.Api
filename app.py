from src.controllers.products import Product
from src.controllers.users import User
from src.controllers.kits import Kit
from src.program.server import server

app = server.app_flask()

if __name__ == "__main__":
    app.run()