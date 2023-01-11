# Author: Milan Seliga*
import pickle 

with open("banner.p" , "rb")  as file:
    unpickled_data = pickle.load(file)

result = ''
for i in unpickled_data:
    for z in range(len(i)):    
        for x in range(int(i[z][1])):
            result += i[z][0]
    result += '\n'

print(result)












# * Jakub Jan Zuber assistance
