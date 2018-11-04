import random

# This returns an array of integers representing the game map
def getMap(filename):
    mapArray = []
    with open(filename) as mapFile:

        # Iterate through mapFile
        for line in mapFile:

            # Get each item from the map
            line = line.strip()
            mapRow = line.split(",")

            # Iterate through mapRow and change each char to an int
            for i, item in enumerate(mapRow):
                mapRow[i] = int(item)
            
            # Append each row to the array
            mapArray.append(mapRow)
        return mapArray

# Generate map
def genMap():
    mapArray = list([])

    # Generate ground level
    for i in range (0, 10):
        mapArray.append([])
        for k in range(0, 100):
            mapArray[i].append(-1)

            if i == 6:
               mapArray[i][k] = 0
    
    # Add obstacles
    for i in range(0, 10):
        for k in range(0, 100):
            if k == random.randint(10, 90) and i < 4:
                mapArray[i][k] = 2

    
    return mapArray


