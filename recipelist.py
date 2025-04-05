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
            #    print(f'{num}. INNN {some_list[index]}')
             #   print(f'result: {f'{num} ' in some_list[index]}')
           # print(some_list[index])
                if some_list[index] in self.smaller_list:
                    skip = 0
                elif f'{num}. ' in some_list[index]:
                    self.smaller_list.append(some_list[index])
                
           

        print(self.smaller_list)
        self.dic_sorted_list(self.smaller_list)

    def dic_sorted_list(self, ing_list):
        for item in ing_list:
            if '*' in item:    #if its formatted like 1. **Onion:** price
                   nitem = item[6:]
                   nitem.replace('*', '')
                   print(nitem)

                 #  self.recipe_cost_dictionary[item_ing] = [item_price]
                   
                   
                                #sort that way
           # else:               #else assume its formatted like 1. Onion: Price





