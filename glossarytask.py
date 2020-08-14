vocab = ["analyse","assess","calculate","comment","compare","complete","consider","contrast","define","demonstrate","describe","develop","discuss","draw","evaluate","examine","explain","give","identify","justify","outline","predict","sketch","state"]
definition = ["examine in detail to show meaning, identify elements and the relationship between them","make an informed judgement","work out from given facts, figures or information","give an informed opinion","identify/comment on similarities and/or differences","add information to an incomplete diagram or table","review and respond to given information","identify/comment on differences","give precise meaning","show how or give an example","state the points of a topic / give characteristics and main features","take forward to a more advanced stage or build upon given information","write about issue(s) or topic(s) in depth in a structured way","draw a line to match a term with a description","judge or calculate the quality, importance, amount, or value of something","investigate closely, in detail","set out purposes or reasons / make the relationships between things evident / provide why and/or how and support with relevant evidence","produce an answer from a given source or recall/memory","name/select/recognise","support a case with evidence/argument","set out main points","suggest what may happen based on available information","make a simple freehand drawing showing the key features, taking care over proportions","express in clear terms"]
import random
points = 0

for x in range(int(input("how many q's do you want?: "))):
    rnum = random.randint(0,24)
    print("#",x+1,"     [ define",vocab[rnum],"]")
    answer = input("defintion: ")
    if answer == definition[rnum]:
        points += 1

print("\n----------------------------")
print("Your total score is:",points)
print("----------------------------\n")



