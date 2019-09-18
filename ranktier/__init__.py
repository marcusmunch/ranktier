class Rank(object):

    def __init__(self, rank):
        if rank == 'null':
            print("This profile has not yet calibrated!")
            self.rank = None
            return

        if type(rank) is int or type(rank) is float:
            rank = str(rank)

        if not all([rank.isdigit(), len(rank) == 2]):
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

        ranks = {"1": "Herald",
                 "2": "Guardian",
                 "3": "Crusader",
                 "4": "Archon",
                 "5": "Legend",
                 "6": "Ancient",
                 "7": "Divine"}

        return "{} [{}]".format(ranks[self.rank[0]], self.rank[1])
