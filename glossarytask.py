vocab = ["analyse","define","describe","explain","outline"]
vocab2 = ["abstraction","decomposition","stepwise refinement","structured english","flowcharts","sequence","selection","iteration"]
import random

for x in range(int(input("how many q's do you want?: "))):
    print("#",x+1,"[",vocab[random.randint(0,4)],vocab2[random.randint(0,7)],"]")
