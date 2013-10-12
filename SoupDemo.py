from bs4 import BeautifulSoup
import urllib2
import csv

NutritionValues = {'Calories', 'Total Fat', 'Sat. Fat', 'Trans Fat', 'Cholesterol', 'Sodium', 'Tot. Carb.', 'Dietary Fiber', 'Sugars', 'Protein', 'Vitamin C', 'Calcium', 'Iron'}

class NutFacts:
    """def __init__(self, Calories, TotalFat, SatFat, TransFat, Cholesterol, Sodium, TotCarb, DietFib, Sugars, Protein, VitC, Calcium, Iron):
        self.calories = Calories
        self.totfat = TotalFat
        self.satfat = SatFat
        self.transfat = TransFat
        self.chol = Cholesterol
        self.sod = Sodium
        self.totcarb = TotCarb,
        self.dietfib = DietFib
        self.sugars = Sugars
        self.protein = Protein
        self.vitc = VitC
        self.calcium = Calcium
        self.iron = Iron
    def __init__(self, NutFactList):
        self.list = NutFactList
        """
    def __init__(self, NutFactDict):
        self.dict = NutFactDict

class Item:
    def __init__(self, Name, NutritionFacts, Veg):
        self.name = Name
        self.nutfacts = NutritionFacts
        self.veg = Veg

class DiningCommon:
    def __init__(self, Name, ItemList):
        self.name = Name
        self.list = ItemList

def getmenu(Name, MealType):
    ItemList = []
    url = "http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    value = soup.find('td')
    for _ in range(assign_num(Name)):
        value = find_next_mealtype(value, MealType)
    ItemList = process_items(value)
    return DiningCommon(Name, ItemList)

#get all the items and their information from the td element value
def process_items(value): #value should be a td element that contains all the items for that meal
    ItemList = []
    links = value.find_all('a')
    if links == []:
        return ('Closed', None, None)
    for link in links:
        NutFactObject = processnutfacts('http://services.housing.berkeley.edu/FoodPro/dining/static/' + link.get('href'))
        ItemName = link.contents[0].contents[0].string
        print(link.contents[0].contents[0])
        if link.contents[0].get('color') == '#000000':
            veg = False
        else:
            veg = True
        ItemList.append(Item(ItemName, NutFactObject, veg))
    return ItemList
        
#find the td element that contains the menu items for that meal
def find_next_mealtype(value, mealtype):
    while mealtype.lower() not in value.find_next('b').string.lower():
        value = value.find_next('td')
    return value

#dining commons appear in this order
def assign_num(name):
    if name.lower() == 'crossroads':
        return 1
    elif name.lower() == 'cafe 3':
        return 2
    elif name.lower() == 'foothill':
        return 3
    else:
        return 4
    
def processnutfacts(link):
    NutFactDict = {}
    url = link
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    value = soup.find('font')
    while value.find_next('font') != None:
        nut_string = value.contents[0].string
        nut_string = nut_string.replace(u'\xa0', u' ').strip()
        if 'Calories' in nut_string and 'Calories from Fat' not in nut_string: #Calories is a special case
            NutFactDict['Calories'] = nut_string[9:]
        elif nut_string in NutritionValues:
            NutFactDict[nut_string] = value.find_next('font').contents[0].string.replace(u'\xa0', u' ').strip()
        value = value.find_next('font')
    return NutFacts(NutFactDict)

            

"""Write into from Soup Demo to file"""
def write(DC):
    ofile = csv.writer(open('test.csv', "wb"))
    ofile.writerow = (["name","vegan","calories","totalfat","satfat","transfat","cholesterol","sodium","totalcarbs","dietfib","sugar","protein","vitc","calcium","iron"])
    for x in DC.list:
        row = []
        row.append(x.name.toString())
        row.append(x.veg.toString())
        for y in x.nutfacts:
            row.append(y.toString())
        ofile.writerow(row)
    ofile.close()            
            
