from app import create_app,db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.auth.v1.models.user_models import User,Pizza,Order

app = create_app('development')

manager=Manager(app)
manager.add_command('server', Server)
migrate= Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Pizza=Pizza, Order=Order)

if __name__ ==' __main__':
    manager.run()