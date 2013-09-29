from bs4 import BeautifulSoup
import urllib2

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
    url = "http://services.housing.berkeley.edu/FoodPro/dining/static/DiningMenus.asp?dtCurDate=9/28/2013&strCurLocation=01&strCurLocationName=" + Name.upper()
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    for link in soup.find_all('a'):
        if 'label.asp?locationNum' in link.get('href'):
            NutFactObject = processnutfacts('http://services.housing.berkeley.edu/FoodPro/dining/static/' + link.get('href'))
            ItemName = link.contents[0].contents[0].string
            if link.contents[0].contents[0].get('color') == '#000000':
                veg = False
            else:
                veg = True
            ItemList.append(Item(ItemName, NutFactObject, veg))
    return DiningCommon(Name, ItemList)
            
            
    
def processnutfacts(link):
    NutFactDict = {}
    url = link
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    for value in soup.find_all('font'):
        nut_string = value.contents[0].string
        if 'Calories' in nut_string and 'Calories from Fat' not in nut_string: #Calories is a special case
            NutFactDict['Calories'] = nut_string[14:]
        elif nut_string[:-1] in NutritionValues:
            NutFactDict[nut_string] = value.find_next('font').contents[0].string[:-1] #last character is g for grams, must index that out
    return NutFacts(NutFactDict)

            
            
            
