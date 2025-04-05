"""test here
"""


from gemini import Gemini

from recipelist import RecipeList

#meals_in_week = int(input('How many meals for a week?: '))
user_food = input('What meals would you like recipes for?: (input as \'chicken pot pie, chicken fried rice, avocado toast\') ')

g_list = RecipeList(Gemini().cost_and_ing(user_food))

g_list.print_dict()
#print(g_list)

#from user_interactiom import userInteract
#good_input = False
#while good_input is False:
 #   try: 
  #      meal_per_week = int(input('How many meals would you like per week?: '))
   #     if meal_per_week <= 0:
    #       raise ValueError
     #   good_input = True
    #except:
     # print('You can\'t have less or equal to 0 meals per week.')


recipes = []

meal_count = 0
#for _ in range(meal_per_week): #is this what u say lol
 #           meal_count += 1
  #          recipes.append(input(f'What meal do you want to prep? (Meal {meal_count}): ')) # could make a suggested:


