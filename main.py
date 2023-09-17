import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    print(client)
    db = client['employees']
    collection = db['sample']
    dictionary = {'name':'aaa', 'age':44, 'salary':50000}
    collection.insert_one(dictionary)