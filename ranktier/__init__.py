def ranktier(rank):
    if rank == 'null':
        print "This profile has not yet calibrated!"
        return None

    if type(rank) is int or type(rank) is float:
        rank = str(rank)

    if not all([rank.isdigit(), len(rank) == 2]):
        print("Something went wrong!\nRank input: %s\n" % rank)
        return None

    return getrank(rank)


def getrank(rank):
    readable_rank = []

    if rank[0] == "1":
        readable_rank.append("Herald")
    elif rank[0] == "2":
        readable_rank.append("Guardian")
    elif rank[0] == "3":
        readable_rank.append("Crusader")
    elif rank[0] == "4":
        readable_rank.append("Archon")
    elif rank[0] == "5":
        readable_rank.append("Ancient")
    elif rank[0] == "6":
        readable_rank.append("Legend")
    elif rank[0] == "7":
        readable_rank.append("Divine")
    else:
    	raise ValueError("Rank '%s' is out of range!" % rank)

    readable_rank.append("[%s]" % rank[1])

    return " ".join(readable_rank)