from math import sqrt

def pathlength(x,y):
    if(len(x) < 1):
        raise ValueError("List Parameters must contain at least one element.")
    previous_x = float(x[0])
    previous_y = float(y[0])
    runningTotalDistance = 0
    #Writing it this way so that the function will still work with only one coordinate pair
    for xi,yi in zip(x,y):
        runningTotalDistance += sqrt( (float(xi) - previous_x)**2 + (float(yi) - previous_y)**2 )
        print runningTotalDistance
    return runningTotalDistance

def test_pathlength():
    xList = [0,3,8,0,-3]
    yList = [0,4,16,1,-3]
    targetPathLength = 5 + 13 + 17 + 5 #pythagorean triples
    assert(pathlength(xList,yList) == targetPathLength)
    return
