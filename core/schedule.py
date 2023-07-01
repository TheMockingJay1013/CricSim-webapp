import random
from datetime import datetime, timedelta


class Schedule:
    def __init__(self):
        self.matches = []
        self.teams = []
        self.venues = []

    def add_match(self, match):
        if len(match) == 2:
            home, away = match
            venue = ""
            date = ""
            time = ""
            self.matches.append((home, away, venue, date, time))
        else:
            self.matches.append(match)

    def add_team(self, team):
        self.teams.append(team)

    def add_venue(self, venue):
        self.venues.append(venue)

    def generate_schedule(self):
        random.shuffle(self.teams)

        global match_count
        match_count = len(self.teams) * (len(self.teams) - 1) // 2
        mid_point = len(self.teams) // 2

        for i in range(match_count):
            round = []
            for j in range(mid_point):
                home = self.teams[j]
                away = self.teams[-j-1]
                if i % 2 == 0:
                    round.append((home, away))
                else:
                    round.append((away, home))
            self.add_round(round)
            self.teams.insert(1, self.teams.pop())

    def add_round(self, round):
        for match in round:
            self.add_match(match)