import json
class TeamsDatabase:
    def __init__(self, teams):
        self._teams = teams

    def teams(self):
        try:
            output = [self._create_team(**data) for data in self._teams]
        except Exception as e:
            print(e)
            return
        sorted_output = sorted(output, key=lambda x: (x.points, x.run_rate), reverse=True)
        json_output = json.dumps(sorted_output, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        parsed_output = json.loads(json_output)  
        return parsed_output

    def _create_team(self, name, matches, won, lost, tied, run_rate, points):
        return Team( name, matches, won, lost, tied, run_rate, points)


class Team:
    def __init__(self, name, matches, won, lost, tied, run_rate, points):
        self.name = name
        self.matches = matches
        self.won = won
        self.lost = lost
        self.tied = tied
        self.run_rate = run_rate
        self.points = points

