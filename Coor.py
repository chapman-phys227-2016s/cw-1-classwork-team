def genCoorList(a, b, n):
    delta = (b-a)/n
    coordinateList = [(a+i*delta) for i in range(int(n+1))]
    return coordinateList

def test_endPoints():
    a = 1
    b = 10
    n = 3
    testList = genCoorList(a,b,n)
    assert (testList[0] == a) and (testList[-1] == b)

def test_delta():
    a = 1
    b = 9
    n = 10
    testList = genCoorList(a,b,n)
    assert ((testList[1] - testList[0] - 0.8) < 0.01)


