from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import *

client = MongoClient('localhost', 27017)
db = client['users']
#db2 = client['books']
persons = db.persons
duplicates = db.duplicates
#
# # doc = {"_id": "67899877665543",
# #        "author": "Peter",
# #        "age": 38,
# #        "Text": "is cool! Wildberry",
# #        "tags": ['cool', 'hot', 'ice'],
# #        "date": '14.06.1983'}
# #
# # try:
# #        persons.insert_one(doc)
# # except DuplicateKeyError as e:
# #        print(e)
#
# # author_list = [{"author": "John",
# #               "age": 29,
# #               "text": "Too bad! Strawberry",
# #               "tags": 'ice',
# #               "date": '04.08.1971'},
#
#               #   {"_id": 123,
#               #    "author": "Anna",
#               # "age": 36,
#               # "title": "Not cool!!!",
#               # "text": "easy too!",
#               # "date": '26.01.1995'},
#               #
#               #        {"author": "Jane",
#               # "age": 43,
#               # "title": "Nice book!",
#               # "text": "Pretty text not long!",
#               # "date": '08.08.1975',
#               # "tags": ['fantastic', 'criminal']}]
#
# #persons.insert_many(author_list)
#     # for author in author_list:
#     #     try:
#     #         persons.insert_one(author)
#     #     except DuplicateKeyError as e:
#     #         duplicates.insert_one(author)
#
# result = persons.find()
#
# # for doc in persons.find({"$or": [{'author':'Peter'}, {'age': 38}]}):
# #     print(doc)
#
# # for doc in persons.find({'age': {$gt: 38}}):
# #     print(doc)
#
# # for doc in persons.find({"$or": [{'author':'Peter'}, {'age': {$gt: 38}}]}):
# #     print(doc)
#
# # for doc in persons.find({"$or": [{'author':'Peter'}, {'age': 38}]}).sort('age', -1):
# #     print(doc)
#
# #persons.update_one({'author': 'Peter'}, {'$set': {'author': 'Petya'}})
# #    print(doc)
#
# #for doc in persons.find():
# #    print(doc)
#
# new_data = {
#     "author": "Andrey",
#     "age": 28,
#     "text": "is not",
#     "date": '11.09.1991'}
#
# #persons.update_one({'author': 'Peter'}, {'$set': new_data})
# persons.replace_one({'author': 'Andrey'},  new_data)
#
# #persons.delete_one({'author': 'John'})
# #persons.delete_many({'author': 'John'})
#
#
# for doc in persons.find():
#     print(doc)


# import requests
#
# response = requests.get("https://gbcdn.mrgcdn.ru/uploads/asset/5560965/attachment/357f7ccb20abaeedb8ccfda8e1045098.json")
#
# with open('data.json', 'wb') as f:
#     f.write(response.content)

import json
from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import *

client = MongoClient('localhost', 27017)
db = client['craches']
info = db.info

# info.delete_many({})
# with open('data.json', 'r') as f:
#     data = json.load(f)
#
# count_duplicated = 0
#
# for feature in data['features']:
#     _id = feature.get('properties').get('tamainid')
#     feature["_id"] = _id
#     try:
#         info.insert_one(feature)
#     except:
#         count_duplicated += 1
#         print(feature)

# print(count_duplicated)
#count = info.count_documents({})
#
# print()
# for doc in info.find({'properties.lat2': {'$gt': 35.0, '$lt': 36.0},
#                       'properties.lon2': {'$gt': -78.0, '$lt': -77.0}}):
for doc in info.find({'properties.tamainid': 48540}):
    print(doc)

#         update_one(upsert)
