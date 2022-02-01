import units

# Dict building/reading
def mapCacheRead(doc):
  d = dict()
  with open(doc) as f: 
    data = f.readlines()
    data = data.split('  ')
    for map in data:
        info = map.split(' ,')
        d[info[0]] = info[1:]

    print(d)
    return (d)

def mapCacheWrite(d, doc):
  with open(doc, 'w') as f:
    for name in d:
        f.write(name)
        f.write(' ')
        map = d[name]
        count = 0
        for row in map:
            f.write(',')
            f.write(row[count])
            count += 1
        f.write('  ')

class tile(object):
    def __init__(self, defence, res, avoid, heal, flyingOnly):
        self.defence = defence
        self.res = res
        self.avoid = avoid
        self.heal = heal
        self.mc = mc
        self.flyingOnly = flyingOnly

#https://fireemblem.fandom.com/wiki/Terrain#Fire_Emblem:_Radiant_Dawn
bog = tile(0, 0, 0, 0, False)
castle = tile(0, 0, 0, 10, False)
fort = tile(0, 0, 0, 10, False)
hall = tile(0, 0, 0, 10, False)
cliff = tile(0, 0, 0, 0, False)
lava = tile(0, 0, 0, 0, False)
coast = (10, 1, 0, 0, False)
trail = (10, 1, 0, 0, False)
wasteland = (10, 1, 0, 0, False)
cover1 = (0, 10, 0, 0, True)
cover2 = (5, 15, 0, 0, True)
cover3 = (0, 10, 0, 0, True)