from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect

class Config(object):
	#项目的配置
	DEBUG =  True

	#s数据库的配置信息
	SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:mysql@127.0.0.1:3306/information"
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# redis配置
	REDIS_HOST = "127.0.0.1"
	REDIS_PORT = 6379

app = Flask(__name__)

#加载配置
app.config.from_object(Config)

#初始化数据库
db = SQLAlchemy(app)

#初始化 redis 存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
#开启当前项目 CSRF 保护，只做服务器验证功能
CSRFProtect(app)


@app.route('/')
def index():
	return 'index'


if __name__ == '__main__':
	app.run(debug = True)
