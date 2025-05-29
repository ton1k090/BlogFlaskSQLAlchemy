from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Создать приложение
app = Flask(__name__)
# Конфигуоация postgres
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:123456@127.0.0.1/news'
UPLOAD_FOLDER = 'static/images' # Где хранить картинки
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Добавить конфиг хранения картинок
app.config['SECRET_KEY'] = 'Very Secret Key'
# Создать БД
db = SQLAlchemy()
# Инициализировать БД
db.init_app(app)
migrate = Migrate(app, db)