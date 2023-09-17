import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    print(client)
    db = client['employees']
    collection = db['sample']
    insertion_list = [{'name': 'aaa', 'age': 44, 'salary': 10000},
                  {'name': 'bbb', 'age': 28, 'salary': 20000},
                  {'name': 'ccc', 'age': 66, 'salary': 30000},
                  {'name': 'ddd', 'age': 35, 'salary': 40000}]
    collection.insert_many(insertion_list)