import sys
# sys.path.insert(0, "./utils")
from utils import teams as te
from utils import teamdetails as td
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# Select the database
db = client['cricket']

# Select the collection


def get_team():
    a = db.IPL.find('',{"_id":0,"team1":1,"team2":1})
    res=[]
    print(a)
    team_list = []
    for i in a:
        res.append(i["team1"])
        res.append(i["team2"])
    print(res)
    teamSet = set(res)

    for team in teamSet:
        res = db.IPL.find({ "$or": [{"team1": team}, {"team2": team}] }, { "_id": 0, "won_by": 1, "match_type": 1 } )
        lost = 0
        won = 0
        tied = 0
        for i in res:
            if i['match_type']=='result':
                if i['won_by']==team:
                    won+=1
                else:
                    lost+=1
            elif i['match_type'] in ['draw','no-result']:
                tied+=1
        team_list.append({'name':team,'won':won, 'lost':lost, 'tied':tied , 'points': won*2+tied, 'matches':won+lost+tied, 'run_rate':0.45})
        
    print(team_list)

    # team_list = [
    #     {
    #         'name': 'Gujrat Titans',
    #         'matches': 14,
    #         'won' : 9,
    #         'lost' : 4,
    #         'tied' : 1,
    #         'run_rate' : 0.45,
    #         'points' : 19,
    #     },
    #     {
    #         'name': 'Chennai Kings',
    #         'matches': 14,
    #         'won' : 8,
    #         'lost' : 5,
    #         'tied' : 0,
    #         'run_rate' : 0.65,
    #         'points' : 17,
    #     },
    #     {
    #         'name': 'Lucknow Giants',
    #         'matches': 14,
    #         'won' : 8,
    #         'lost' : 5,
    #         'tied' : 0,
    #         'run_rate' : 0.48,
    #         'points' : 22,
    #     },
    #     {
    #         'name': 'Mumbai Indians',
    #         'matches': 14,
    #         'won' : 8,
    #         'lost' : 6,
    #         'tied' : 0,
    #         'run_rate' : 0.40,
    #         'points' : 22,
    #     }]

    teams = te.TeamsDatabase(team_list)
    team = teams.teams()
    return team


def get_details(name):
    a=db.IPL.find({ "$or": [{"team1": name}, {"team2": name}] }, { "_id": 0, "description": 1, "date": 1, "result":1, "team1":1, "team2":1 } )
    description = []
    for data in a:
        opponent = data['team2'] if data['team2']!=name else data['team1']
        description.append({'opponent':opponent,'description':data['description'],'date':data['date'],'result':data['result']})
    # description = [{
    #     'opponent':'Chennai Kings',
    #     'description':5,
    #     'date' : '1st may',
    #     'result' : 'won by 5 wkts'
    # },
    # {
    #     'opponent':'Lucknow Giants',
    #     'description':1,
    #     'date' : '31st mar',
    #     'result' : 'won by 50 runs'
    # },
    # {
    #     'opponent':'Mumbai Indians',
    #     'description':21,
    #     'date' : '31st may',
    #     'result' : 'loss by 5 wkts'
    # }
    # ]
    details = td.TeamsDetails(description)
    detail = details.teams()
    return detail
get_team()