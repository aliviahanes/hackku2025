"""test here
"""


from gemini import Gemini

from recipelist import RecipeList

g_list = RecipeList(Gemini().cost_of_ing('five cheese ziti'))

print(g_list)

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



from google import genai

client = genai.Client(api_key="AIzaSyCC50YnW_xy0SfDJkUjRY2aNVisniZmguE")

#response = client.models.generate_content(
 #   model="gemini-2.0-flash", contents="Explain how AI works in a few words"
#)
#print(response.text)

#PNOTE: takes a while to generate, maybe make loading screen ?
response = client.models.generate_content(                                                    
    model="gemini-2.0-flash", contents=f"what are some good meal-prepping meals for {meal_per_week} days"
)

print(response.text)