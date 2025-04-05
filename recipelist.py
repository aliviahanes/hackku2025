'''
this file should break down the Gemini information nicely so we can store it and send it to user in a nice format

'''
from gemini import Gemini

class RecipeList:
    def __init__(self, gem_file):
        self.gem_file = gem_file
        self.giant_list = [] #might want to break down into ingredient and price list?
        self.recipe_cost_dictionary = {}
        self.smaller_list = []
        self.read()


#READING FILE BASED ON HOW GEMINI GIVES IT TO US, gives it to us diff every time tho?
    def read(self):
       # skip_first_three_lines = 0
        line = self.gem_file.split('\n')
        print(line)

        self.sort_glist(line)
    

    def sort_glist(self, some_list):
        for index in range(len(some_list)):
            for num in range(len(some_list)):
                print(f'{num}. INNN {some_list[index]}')
                print(f'result: {f'{num} ' in some_list[index]}')
           # print(some_list[index])
                if f'{num}. ' in some_list[index]:
                    self.smaller_list.append(some_list[index])
           

        print(self.smaller_list)





