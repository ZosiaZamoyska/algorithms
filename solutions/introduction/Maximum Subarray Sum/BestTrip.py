'''
    There are n cities along the railway tracks. 
    A sandy, one-way road also runs through the cities. 
    The road is divided into sections, each of which connects two neighbouring cities. 
    A boy would like to get from the first city to the last one and would like to earn as much as possible.
    The boy earns money by selling goods. 
    He knows exactly how much he will earn or lose on each section of the sandy road. 
    He does not have to travel each section of the road, because he has one train ticket, which he can use on any part of the road (i.e. get on in a certain city and get off in any other, possibly earlier). 
    The train runs in both directions, and the boy, by covering a section of the road again, will earn or lose the same amount as before.
    The boy would like to plan his journey in advance. 
    Help him and tell him how much he can earn at most.

    There is z <=20 different test sets, with n <= 100,000 cities.

    Example:
    2
    3
    -1 -1
    5
    3 5 5 2

    Answer
    0
    30
'''
def best_trip(n, arr):
    pref, maxpref = 0, 0
    suf, maxsuf = 0, 0
    
    for i in range(n-1):
        pref += arr[i]
        maxpref = max(maxpref, pref)
    
    for i in range(n-2, -1, -1):
        suf += arr[i]
        maxsuf = max(maxsuf, suf)
    
    return maxpref + maxsuf

z = int(input())
for _ in range(z):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    #n = 5
    #arr = [3, 5, 5, 2]
    print(best_trip(n, arr))
