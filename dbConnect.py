from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml

# Load the database configuration from the file
with open('application-secret.yaml', 'r') as f:
    dbConfig = yaml.safe_load(f)

userName = dbConfig['db']['userName']
password = dbConfig['db']['password']
host = dbConfig['db']['host']
port = dbConfig['db']['port']
dbName = dbConfig['db']['dbName']


url = "mysql+pymysql://'{userName}':'{password}'@{host}:{port}/{dbName}?charset=utf8".format(userName=userName, password=password, host=host, port=port, dbName=dbName)
print('')
print('url: ', url)
print('')

engine = create_engine(url, echo=True)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print('session: ', session)
