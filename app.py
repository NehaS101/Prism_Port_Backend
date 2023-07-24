from config.db import connection
from flask import Flask
import os
from flask_cors import CORS
from routes.manager_route import manager_router
from routes.project_route import project_router
from routes.task_route import task_router
from routes.resuorce_route import resource_router
from routes.login_route import login_router
from routes.signup_route import signup_router

app = Flask(__name__)
CORS(app)
app.debug = True

#home route
@app.route('/', methods=['GET'])
def welcome():
    return ('Welcome to prism port application!')

#routers
app.register_blueprint(manager_router,url_prefix='/manager')
app.register_blueprint(project_router,url_prefix='/project')
app.register_blueprint(task_router,url_prefix='/task')
app.register_blueprint(resource_router,url_prefix='/resource')
app.register_blueprint(login_router)
app.register_blueprint(signup_router)

if __name__ == '__main__':
    connection()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
