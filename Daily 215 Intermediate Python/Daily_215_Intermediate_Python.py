import itertools

def medium215(network_file="input.txt"):
    intext = open(network_file)
    #Generate test cases
    networkParams=intext.readline()
    networkParams=[int (x) for x in networkParams.split()]

    tests=list(itertools.product([0,1],repeat=networkParams[0]))

    network=[]
    for line in intext:
        network.append(line)

    for test in tests:
        test=list(test) #Itertools gives tuples, change test from tuple to list
        for junction in network:
            cands=[int (x) for x in junction.split()]
            if test[cands[0]] > test[cands[1]]: #If they're out of order, swap
                test[cands[0]],test[cands[1]] = test[cands[1]], test[cands[0]]

        if not isSorted(test):
            print ("Failure.  Returned: ",test)
            return False
    return True

def isSorted(test):
    for i in range(len(test)-1):
        if test[i]>test[i+1]:
            return False
    return True