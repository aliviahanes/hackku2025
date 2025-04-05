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
        model="gemini-2.0-flash", contents=f"Give me JUST the estimated cost of ingredients for {foods}, combine ingredients and list them all out in a numbered list with cost, make sure to number the ingredients. This list should be optimized so that only the minimum number of ingredients are listed. List all ingredients in one list, do NOT separate them by meal. The formatting for one item should look like this: 1. *swiss cheese*: $6.00. If multiple packs of an item are needed, adjust the name and cost(where cost is the multiple of the base price by the quantity) to match the format of: 2. *2x swiss cheese* $18.00"
        )
        # #f"Give me JUST the estimated cost of ingredients for {foods}, combine ingredients (ex. if need onion for recipe1 and recipe2, i just need to list onion once) and list them all out in a numbered list with cost, make sure to number the ingredients, organize list like grocery store"
        

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
make sure to number the ingredients. This list should be optimized so 
that only the minimum number of 
ingredients are listed. List all ingredients in one list, 
do NOT separate them by meal. The formatting for one item should 
look like this: 1. *swiss cheese*: $6.00
This list should be optimized so that only the minimum number of 
ingredients are listed. List all ingredients in one list, 
do NOT separate them by meal. The formatting for one item should 
look like this: 1. *swiss cheese*: $6.00. 
If multiple packs of an item are needed, adjust the name and 
cost(where cost is the multiple of the base price by the quantity)
to match the format of: 2. *2x swiss cheese* $18.00"   
'''
  #  def list_of_ing(self, food):