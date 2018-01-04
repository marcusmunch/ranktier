def ranktier(rank):
    if rank == 'null':
        print("This profile has not yet calibrated!")
        return None

    if type(rank) is int or type(rank) is float:
        rank = str(rank)

    if not all([rank.isdigit(), len(rank) == 2]):
        print("Something went wrong!\nRank input: %s\n" % rank)
        return None

    return getrank(rank)


def getrank(rank):
    readable_rank = []

    ranks = { "1" : "Herald"
            , "2" : "Guardian"
            , "3" : "Crusader"
            , "4" : "Archon"
            , "5" : "Legend"
            , "6" : "Ancient"
            , "7" : "Divine" }

    readable_rank.append("[%s]" % rank[1])

    return "{} [{}]".format(ranks[rank[0]], rank[1])
