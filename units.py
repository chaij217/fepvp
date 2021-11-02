# Based on FE10
#https://fireemblem.fandom.com/wiki/List_of_classes_in_Fire_Emblem:_Radiant_Dawn
class Unit():
    def __init__ Unit(self):
        self.pos = None

    def statLoad(self, data):
        self.name = data[0]
        self.clss = data[1]
        self.lv = data[2]
        self.hp = [data[3], data[3]]
        self.str = data[4]
        self.mag = data[5]
        self.skl = data[6]
        self.spd = data[7]
        self.lck = data[8]
        self.df = data[9]
        self.res = data[10]
        self.con = data[11]
        self.wt = data[12]
        self.mov = data[13]
    
    def classStats(self):
        d = dict()
        d['hero'] = ([['sword'], ['S']], set(['shove']))
        d['vanguard'] = ([['sword', 'axe'], ['SS', 'SS']], set('shove', 'aether'))
        d['myrmidon'] = ([['sword'], ['D']], set('shove', 'crit+5'))
        d['swordmaster'] =  