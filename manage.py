from flask_script import Manager, Server
from flablo import app

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=2222, use_debugger=True))

if __name__=='__main__':
    manager.run()
