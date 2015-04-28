"""
bar = 2d array
hotSites = list of Coordinates of hot
coldSites = list of coordinates of cold

"""
def applyHotCold(bar, hotSites, coldSites):
    newBar = bar
    count = 0
    while count < len(hotSites):
        newBar[hotSites[0]][hotSites[1]] = HOT
        count += 1
    count = 0
    while count < len(coldSites):
        newBar[coldSites[0]][coldSites[1]] = COLD
        count += 1
    return newBar