from pymongo import MongoClient
a=[
    {'team1': 'Gujrat-Titans',
     'team2': 'Chennai-Kings',
     'description': 2,
     'date': '31 mar',
     'won_by': 'Gujrat-Titans',
     'result':'won by 5 wkts',
     'match_type': 'draw'
      },
      {'team1': 'Gujrat-Titans',
     'team2': 'Lucknow-Giants',
     'description': 3,
     'date': '1 may',
     'won_by': 'Gujrat-Titans',
     'result':'won by 5 wkts',
     'match_type': 'no-result'
      },
     { 'team1': 'Gujrat-Titans',
     'team2': 'Mumbai-Indians',
     'description': 1,
     'date': '31 mar',
     'won_by': 'Mumbai-Indians',
     'result':'won by 5 wkts',
     'match_type': 'result'}
]
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Select the database
db = client['cricket']

# Select the collection
collection = db['IPL']

# Create a document
for data in a:
# Insert the document into the collection
    result = collection.insert_one(data)

# Print the inserted document's ID
    print('Inserted document ID:', result.inserted_id)
a = db.IPL.find('',{"_id":0,"team1":1,"team2":1})
res=[]
print(a)
for i in a:
    res.append(i["team1"])
    res.append(i["team2"])
print(res)
