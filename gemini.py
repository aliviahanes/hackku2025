"""
gemini class?
"""
from google import genai

class Gemini:
    def __init__(self):
        self._client = genai.Client(api_key="AIzaSyCC50YnW_xy0SfDJkUjRY2aNVisniZmguE")


    def cost_of_ing(self, food):
        response = self._client.models.generate_content(                              #eventually should be for {user_food} or smthn
        model="gemini-2.0-flash", contents=f"Give me the estimated cost of ingredients for {food} in a numbered list"
        )

        print(response.text)
        return response.text
    
  #  def list_of_ing(self, food):