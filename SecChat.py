from modules.auth_menu import auth_menu
from modules.user_menu import user_menu
from modules.installation import setup_databases

setup_databases()

while True:
    user_menu(auth_menu())