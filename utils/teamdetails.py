import json
class TeamsDetails:
    def __init__(self, teamDetails):
        self._team_details = teamDetails

    def teams(self):
        try:
            output = [self._create_details(**data) for data in self._team_details]
        except Exception as e:
            print(e)
            return
        sorted_output = sorted(output, key=lambda x: (x.description))
        json_output = json.dumps(sorted_output, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        parsed_output = json.loads(json_output)  
        return parsed_output

    def _create_details(self, opponent, description, date, result):
        return Detail( opponent, description, date, result)


class Detail:
    def __init__(self, opponent, description, date, result):
        self.opponent = opponent
        self.description = description
        self.date = date
        self.result = result


