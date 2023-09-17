import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    print(client)
    db = client['employees']
    collection = db['sample']
    one = collection.find({'name': 'aaa'}, {'name': 1, 'salary': 1, "_id": 0})
    for i in one:
        print(i)