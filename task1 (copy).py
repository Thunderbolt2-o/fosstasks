#ROCKPAPERSCISSORGAME

import random
import time

cscore = 0
pscore = 0
choose=("a")

k= ["rock", "paper", "scissor"]

f=0
while (f==0):
	cpu=random.choice(k)
	if (choose=="0"):
		break
#let us play rockpaper scissor
	giving= input("which one you want:")
	print("wait until computer takes")
	time.sleep(2)
	print("the cpu taken is  "+cpu)
	if(giving==cpu):
		print("what a coincindence the game is tied")
	elif (giving==k[0]):
		if (cpu==k[2]):
			print("you won over  opponent"+giving+"blunt"+cpu)
			pscore=pscore+1
		else:
			print("sorry u lost game try next time")
			cscore=cscore+1
	elif (giving==k[1]):
		if (cpu==k[0]):
			print("you won over  opponent"+giving+"covers"+cpu)
			pscore=pscore+1
		else:
			print("sorry u lost game try next time")
			cscore=cscore+1
	elif (giving==k[2]):
		if (cpu==k[1]):
			print("you won over  opponent"+giving+"cutting"+cpu)
			pscore=pscore+1
		else:
			print("sorry u lost game try next time")
			cscore=cscore+1
	else:
		print("u did not select rock,paper,scissor")

	print("if you want to finish ur game press 0")
	choose=input("choose for  to play or not:")
print("cscore is"+str(cscore))
print("pscore is"+str(pscore))
if (cscore>pscore):
	print("ur efforts are over.. come again to challenge ur self as computer wins it")
else:
	print("u are champion of the champion")
	

			










