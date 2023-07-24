from flask import Blueprint
from controllers.signup_controller import (signup)

signup_router = Blueprint('signup',__name__)

signup_router.route('/signup',methods=['POST'])(signup)