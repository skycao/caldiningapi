class User(object):
    """Holds input for the user, namely his or her diet and preferences."""
    def __init__(diet, preferences):
        self.diet = diet
        self.preferences = preferences

class Diet(object):
    
    
    def __init__(calorie_limit, protein_limit, carb_limit, fat_limit, bulking, meat_vege_veg):
      self.bulking = bulking
      self.calorie_limit = calorie_limit
      self.protein_limit = protein_limit
      self.carb_limit = carb_limit
      self.fat_limit = fat_limit
      self.food_type = meat_vege_veg
