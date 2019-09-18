import json
import socket
import sys
import urllib.request

VERSION = 1.4
USER_AGENT = "ranktier/{}".format(VERSION)


class Rank(object):

    def __init__(self, rank, leaderboard=False):
        self.leaderboard = leaderboard

        if rank == 'null':
            print("This profile has not yet calibrated!")
            self.rank = None
            return

        if type(rank) is int or type(rank) is float:
            rank = str(rank)

        if not all([rank.isdigit(), len(rank) == 2]) and not leaderboard:
            print("Something went wrong!\nRank input: %s" % rank)
            self.rank = None
            return

        self.rank = rank

    def __str__(self):
        return str(self.name)

    @property
    def name(self):
        if self.rank is None:
            return None

        if self.leaderboard:
            return "Immortal rank {}".format(self.rank)

        if self.rank[0] == "8":
            return "Immortal"

        ranks = {"1": "Herald",
                 "2": "Guardian",
                 "3": "Crusader",
                 "4": "Archon",
                 "5": "Legend",
                 "6": "Ancient",
                 "7": "Divine"}

        return "{} [{}]".format(ranks[self.rank[0]], self.rank[1])


class Player:

    def __init__(self, friend_id):

        self.friend_id = friend_id
        try:
            profile = self.get_profile_data()
            print(profile)

            self.personaname = profile["profile"]["personaname"]
            if profile["leaderboard_rank"]:
                self.rank = Rank(profile["leaderboard_rank"], leaderboard=True)
            else:
                if not profile["rank_tier"]:
                    self.rank = Rank("null")
                else:
                    self.rank = Rank(profile["rank_tier"])

        except socket.timeout:  # API connection timed out
            sys.stderr.write("Connection to OpenDota API timed out!")

    def get_profile_data(self):
        req = urllib.request.Request(url="https://api.opendota.com/api/players/{}".format(self.friend_id),
                                     headers={"User-Agent": USER_AGENT})

        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read())
            return data
