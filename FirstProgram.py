# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)":"😊",
#     ":(":"🥲"
# }
# output =""
# for word in words:
#     output+=emojis.get(word,word)+" "
# print(output)


# def sqr(n):
#     return n*2
#
# print(sqr(4))

# class Mammal:
#     def bark(self):
#         print("bark")
#
# class Dog(Mammal):
#     pass
#
# class Cat(Mammal):
#     def talk(self):
#         print("meow")
#
#
# dog=Dog()
# dog.bark()
# print("")
# cat=Cat()
# cat.bark()
# cat.talk()


# import converters
# print(converters.lbs_to_kgs(90))

# from converters import lbs_to_kgs
# print(lbs_to_kgs(90))

#
# import converters
# print("maximum number of given numbers is ",converters.maxx([1,2,3,4,5,6,7]))

#
# import random
# leader=random.choice(["Rupesh","Lokesh","Sai","Sandeep"])
# print(leader)

#
# from pathlib import Path
# path=Path("newdir")
# print(path.exists())
#p=Path("em")
# print(p.mkdir())#.....it makes new directiory
#print(p.rmdir())#......it removes the directiory

#
# from pathlib import Path
# path=Path()
# for file in path.glob('*.py'):
#     print(file)

class Questions:
    def __init__(self,promt,answer):
        self.promt=promt
        self.answer=answer


questions_promts=["What is the colour of apple\n","What is colour of banana\n"]

questions=[
    Questions(questions_promts[0],"red"),
    Questions(questions_promts[1],"yellow")
]

def runtest(questions):
    score=0
    for question in questions:
        answer=input(question.promt)
        if answer==question.answer:
            score+=1

    print(f"you got {score}/2 correct")


runtest(questions)