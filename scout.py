import pymongo

class Team:
    """Team class"""
    def __init__(self, team_num):
        """Constructor"""
        self.team_num = team_num

    def get_least_balls_scored(self, results):
        """Calculate least amount of balls scored in a match"""
        min = 10000
        for result in results:
            #print("in least ball")
            #print(result)
            if result['num_balls'] < min:
                min = result['num_balls']
        return min

    def get_most_balls_scored(self, results):
        """Calculates max amount of balls scored in a match"""
        max = 0
        for result in results:
            if result['num_balls'] > max:
                max = result['num_balls']
        return max

    def get_average_balls_scored(self, results):
        """Calculates average balls scored by a team"""
        balls_scored = 0
        matches_played = 0
        for result in results:
            balls_scored += result['num_balls']
            matches_played += 1
        return balls_scored / matches_played

    def get_climb_percentage(self, results):
        """Calculates percentage of successful climbs"""
        climb = 0
        total_climbs = 0
        for climbs in results:
            if climbs['climbed'] == True:
                climb += 1
            total_climbs += 1
        return "{0:.0f}%".format(climb / total_climbs * 100)

    def get_num_of_matches(self):
        """Calculates matches played by a team"""

        return collection.count_documents(myquery)

# Get a connection to MongoClient
client = pymongo.MongoClient("localhost", 27017)
db = client["test"]
collection = db["docs"]
collection_team_stats = db["team_stats"]
# Finds each distinct team in collection
for team_num in collection.find().distinct('team_num'):
    myquery = {"team_num": team_num}
    results = collection.find(myquery)
    team = Team(team_num)
    max_balls = team.get_most_balls_scored(results)
    results = collection.find(myquery)
    min_balls = team.get_least_balls_scored(results)
    results = collection.find(myquery)
    avg_balls = team.get_average_balls_scored(results)
    results = collection.find(myquery)
    climb_percent = team.get_climb_percentage(results)
    results = collection.find(myquery)
    num_of_matches = team.get_num_of_matches()
    # Create a json for each team
    team_stats = {"team_num": team_num, "max_balls": max_balls, "min_balls": min_balls, "avg_balls": avg_balls,
                  "climb_percent":climb_percent, "num_of_matches": num_of_matches}
    # Insert each team into the collection
    collection_team_stats.insert_one(team_stats)



