DIALECT = 'mysql'  # What database to use
DRIVER = 'pymysql'  # Connect to database driver

USERNAME = 'root'  # username
PASSWORD = '123456'  # password
HOST = 'localhost'  # server host
PORT = '3306'  # port
DATABASE = 'inquiry_price'  # database


# Set the URL to connect to the database
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Specifies the configuration to omit the commit operation if one is present in the configuration file. You can comment
SQLALCHEMY_COMMIT_ON_TEARDOWN = True