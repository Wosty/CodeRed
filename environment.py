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
