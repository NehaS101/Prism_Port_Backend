from flask import Blueprint
from controllers.resource_controller import (get_resource,create_resource,delete_resource)

resource_router = Blueprint('resource',__name__)

resource_router.route('/get_resource',methods=['GET'])(get_resource)
resource_router.route('/create_resource',methods=['POST'])(create_resource)
resource_router.route('/delete_resource/<string:resource_id>',methods=['DELETE'])(delete_resource)
