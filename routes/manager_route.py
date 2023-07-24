from flask import Blueprint
from controllers.manager_controller import(
    create_managers,
    getAll_managers,
    get_managers_byId,
    update_managers_byId,
    delete_manager
)

manager_router = Blueprint('manager', __name__)

manager_router.route('/portfolio-managers',methods=['POST'])(create_managers)

manager_router.route('/portfolio-managers',methods=['GET'])(getAll_managers)

manager_router.route('/portfolio-managers/<string:manager_id>',methods=['GET'])(get_managers_byId)

manager_router.route('/portfolio-managers/<string:manager_id>',methods=['PUT'])(update_managers_byId)

manager_router.route('/portfolio-managers/<string:manager_id>',methods=['DELETE'])(delete_manager)

