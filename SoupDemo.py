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

class Item:
    def __init__(self, Name, MealType, NutritionFacts):
        self.name = Name
        self.mealtype = MealType
        self.nutfacts = NutritionFacts

class DiningCommon:
    def __init__(self, Name, ItemList):
        self.name = Name
        self.list = ItemList

