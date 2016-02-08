from random import randint

def minElement(*a):
    if(len(a) > 0):
        minValue = a[0]
        for elem in a:
            if(minValue > elem):
                minVaule = elem
        return minValue
    else:
        raise ValueError("List must be of length greater than 0.")
        
        
def maxElement(*a):
    if(len(a) > 0):
        maxValue = a[0]
        for elem in a:
            if(maxValue < elem):
                maxValue = elem
        return maxValue
    else:
        raise ValueError("List must be of length greater than 0.")
        
def test_againstBuiltInMin():
    randomList = [randint(0,100) for i in range(20)]
    assert(min(randomList) == minElement(randomList))
    return

def test_againstBuiltInMax():
    randomList = [randint(0,100) for i in range(20)]
    assert(max(randomList) == maxElement(randomList))
    return

        