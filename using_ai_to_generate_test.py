from google import genai

client = genai.Client(api_key="AIzaSyCC50YnW_xy0SfDJkUjRY2aNVisniZmguE")

#response = client.models.generate_content(
 #   model="gemini-2.0-flash", contents="Explain how AI works in a few words"
#)
#print(response.text)


response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Give me the estimated cost and list of ingredients for Chicken Noodle Soup"
)

print(response.text)