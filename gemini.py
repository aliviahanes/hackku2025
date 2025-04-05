"""
gemini class,
use this to generate prompts
"""
from google import genai

class Gemini:
    def __init__(self):
        self._client = genai.Client(api_key="AIzaSyCC50YnW_xy0SfDJkUjRY2aNVisniZmguE")


    def cost_and_ing(self, foods):
      #  response = self._client.models.generate_content(                              #eventually should be for {user_food} or smthn
      #  model="gemini-2.0-flash", contents=f"Give me JUST the estimated cost of ingredients for {foods} in a numbered list"
      #  )
        response = self._client.models.generate_content(                                                     #eventually should be for {user_food} or smthn
<<<<<<< HEAD
        model="gemini-2.0-flash", contents=f"Give me JUST the estimated cost of ingredients for {foods}, combine ingredients (ex. if need onion for recipe1 and recipe2, i just need to list onion once) and list them all out in a numbered list with cost, make sure to number the ingredients, organize list like grocery store"
=======
        model="gemini-2.0-flash", contents=f"Give me JUST the estimated cost of ingredients for {foods}, combine ingredients and list them all out in a numbered list with cost, make sure to number the ingredients. This list should be optimized so that only the minimum number of ingredients are listed. List all ingredients in one list, do NOT separate them by meal. The formatting for one ingredient should look like this: 1. *swiss cheese*: $6.00. If multiples of an item are needed, "
>>>>>>> 8ee1d42e79e40599d7fb7875e0127d9db57152f3
        )

        print(response.text)
        return response.text
    
    def sort_by_ing(self,ingredients):
          #  )
        response = self._client.models.generate_content(                                                     #eventually should be for {user_food} or smthn
        model="gemini-2.0-flash", contents=f"sort this list of ingredients by how you would find them in a grocery store"
        )

        print(response.text)
        return response.text


   
'''
Give me JUST the estimated cost of ingredients for {foods}, 
combine ingredients and list them all out in a numbered list with cost,
make sure to number the ingredients. This list should be optimized so that only the minimum number of ingredients are listed. List all ingredients in one list, do NOT separate them by meal. The formatting for one item should look like this: 1. *swiss cheese*: $6.00
    
'''
  #  def list_of_ing(self, food):