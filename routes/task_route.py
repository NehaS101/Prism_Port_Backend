from flask import Blueprint
from controllers.task_controller import (getAll_tasks,create_task,delete_task)

task_router = Blueprint('task',__name__)

task_router.route('/create_task',methods=['POST'])(create_task)
task_router.route('/delete_task/<string:task_id>',methods=['DELETE'])(delete_task)
task_router.route('/get_tasks',methods=['GET'])(getAll_tasks)