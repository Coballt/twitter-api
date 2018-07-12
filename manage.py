from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from wsgi import application

migrate = Migrate(application, application.db)

manager = Manager(application, application.db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
