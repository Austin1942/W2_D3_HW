import math
def measure_home():
    width_of_home = []
    length_of_home = []
    while True:
         question = input("what is the width of your home? ").strip()
         if question == '':
             width_of_home.append()
            
        
         question_2 = input("what is the length of your home? ").strip()
         if question_2 == '':
             length_of_home.append()
         
         total = width_of_home + length_of_home
         atotal = math.prod(total)

         print(atotal)
         break
    return atotal
measure_home()