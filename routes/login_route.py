from flask import Blueprint
from controllers.login_controller import (login)

login_router = Blueprint('login',__name__)

login_router.route('/login',methods=['POST'])(login)