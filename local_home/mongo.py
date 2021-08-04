from pymongo import MongoClient

if __name__ == '__main__':
client= MongoClient('localhost',27017)
db=client['game']
collection=db['test']
