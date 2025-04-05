"""
gemini class?
"""
from google import genai

class Gemini:
    def __init__(self):
        self._client = genai.Client(api_key="AIzaSyCC50YnW_xy0SfDJkUjRY2aNVisniZmguE")


    def cost_of_ing(self, foods):
      #  response = self._client.models.generate_content(                              #eventually should be for {user_food} or smthn
      #  model="gemini-2.0-flash", contents=f"Give me JUST the estimated cost of ingredients for {foods} in a numbered list"
      #  )
        response = self._client.models.generate_content(                                                     #eventually should be for {user_food} or smthn
        model="gemini-2.0-flash", contents=f"Give me JUST the estimated cost of ingredients for {foods}, combine ingredients and list them all out in a numbered list with cost, make sure to number the ingredients"
        )

        print(response.text)
        return response.text
    
    

   
    
  #  def list_of_ing(self, food):