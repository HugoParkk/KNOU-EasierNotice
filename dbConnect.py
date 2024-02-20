from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



url = "mysql+pymysql://'{userName}':'{password}'@{host}:{port}/{dbName}?charset=utf8".format(userName=userName, password=password, host=host, port=port, dbName=dbName)
print('')
print('url: ', url)
print('')

engine = create_engine(url, echo=True)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print('session: ', session)
