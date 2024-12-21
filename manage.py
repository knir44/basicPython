import os
from flask_script import Manager
import unittest
from app import blueprint
from app.main.init__ import create_app


app = create_app()
app.register_blueprint(blueprint)

app.app_context().push()
manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()