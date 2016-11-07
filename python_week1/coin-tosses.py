import random
heads = 0
tails = 0


for toss in range (1, 5000):
    random_num = random.random()
    if random_num >= .5:
        heads +=1
        print "Attempt #%s: Throwing a coin... It's a head! ... Got %s  head(s) so far and %s  tail(s) so far" % (toss, heads, tails)
    else:
        tails+=1
        print "Attempt #%s: Throwing a coin... It's a tail! ... Got %s  head(s) so far and %s  tail(s) so far" % (toss, heads, tails)
