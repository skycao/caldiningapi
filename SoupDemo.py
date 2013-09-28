from bs4 import BeautifulSoup
import urllib2

class NutFacts:
    def __init__(self, TotalFat, SatFat, TransFat, Cholesterol, Sodium, TotCarb, DietFib, Sugars, Protein, VitC, Calcium, Iron):
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
    def __init__(self, NutFactDict):
        self.dict = NutFactDict

class Item:
    def __init__(self, Name, MealType, NutritionFacts):
        self.name = Name
        self.mealtype = MealType
        self.nutfacts = NutritionFacts

class DiningCommon:
    def __init__(self, Name, ItemList):
        self.name = Name
        self.list = ItemList

def getmenu(Name, MealType):
    url = "http://services.housing.berkeley.edu/FoodPro/dining/static/DiningMenus.asp?dtCurDate=9/28/2013&strCurLocation=01&strCurLocationName=" + Name.upper()
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    for link in soup.find_all('a'):
        if 'label.asp?locationNum' in link.get('href'):
            
    
    

