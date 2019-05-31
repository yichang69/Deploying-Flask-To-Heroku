from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://rjljnrlvtrgiar:90fd49516ec2c2cee2c0333f472393ec6c667e55edf2509699e6b62b1133da93@ec2-54-163-226-238.compute-1.amazonaws.com:5432/d3hbcuqde7u5cu'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class UserData(db.Model):
    __tablename__ = 'UserData'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Description = db.Column(db.String(256))
    CreateDate = db.Column(db.DateTime)

    def __init__(self
                 , Name
                 , Description
                 , CreateDate
                 ):
        self.Name = Name
        self.Description = Description
        self.CreateDate = CreateDate


if __name__ == '__main__':
    manager.run()
