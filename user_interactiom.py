""""
ask user for how many meals per week they want to meal prep
    ask for recipes
"""

class userInteract:     #int            #str
    def __init__(self, meal_per_week):
        self.meal_per_week = self.meal_per_week
        self.recipes = []

    def ask_questions(self): #lowkey why is this a method 
        meal_count = 0
        for _ in range(self.meal_per_week): #is this what u say lol
            meal_count += 1
            self.recipes.append(input(f'What meal do you want to prep? (Meal {meal_count}): '))