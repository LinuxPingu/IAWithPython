from typing import List
import random
from sympy import Matrix

endUserLoop = False
userToEval = ""

def GetRandomRatings() -> List[int]:
    return [random.randint(1,5),random.randint(1,5),random.randint(1,5),random.randint(1,5)]

#Change to default values to test the homework
ratings = {
    "Juan": GetRandomRatings(),
    "Ana": GetRandomRatings(),
    "Carlos": GetRandomRatings()
}

def PrintRatings():
    for name, rating in ratings.items():
     print(f"Current ratings of user {name}: {rating}")

while endUserLoop == False:
    try:
        PrintRatings()
        user_input = input(f"From the list, type a name to evaluate ratings: ")
        if user_input in ratings:
            userToEval = user_input
            endUserLoop = True
        else:
            print(f"please check the input provided")
    except:
        print(f"please check the input provided")

prox = 0.0
proxKey = ""
evalMatrix = Matrix(ratings.get(userToEval))

for name, rating in ratings.items():
    if name != userToEval:
        tempMatrix = Matrix(ratings.get(name))
        product = evalMatrix.dot(tempMatrix)
        if prox < product:
            proxKey = name
            prox = product

print(f"Most similar user {proxKey}: {prox}")

ratings["Rei"] = [5,0,3,0]
print(f"Adding new user...")
PrintRatings()
        
        



    
    






