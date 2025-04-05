'''
this file should break down the Gemini information nicely so we can store it and send it to user in a nice format

'''

class RecipeList:
    def __init__(self, gem_file):
        self.gem_file = gem_file
        self.giant_list = [] #might want to break down into ingredient and price list?
        self.recipe_cost_dictionary = {}
        self.read()


#READING FILE BASED ON HOW GEMINI GIVES IT TO US, gives it to us diff every time tho?
    def read(self):
        skip_first_three_lines = 0
        for line in self.gem_file:
            if skip_first_three_lines == 0 or skip_first_three_lines == 1 or skip_first_three_lines == 2:
                skip_first_three_lines += 1 #LeAVE FOR NOW HIS jUST BASICS
            else:
                line = line.strip()
                self.giant_list.append(line) #giant list without first three things, other useless things in gemini response but fix later

    def organize_giant_list(self):# store in dictionaries? just print?
        for item in self.giant_list:
            #somehow fix the * ** part
            #this just basics                                       #how we assign price to correct ingrecdient
            self.recipe_cost_dictionary[item] = self.giant_list[]




