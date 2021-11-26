import random
import copy

def heuristic(start_state,goal_state):

	diff = 0
	
	for i in range(len(start_state)):
	
		diff += abs(ord(start_state[i]) - ord(goal_state[i]))
		
	return(diff)
	 

def createchild(cur_state,goal_state):

	wordlist = [chr(i) for i in range(97,123,1)]
	
	tempchild = []
	
	for i in range(len(cur_state)):
	
		if(cur_state[i] != goal_state[i]):
		
			tempchild = copy.deepcopy(cur_state)
			tempchild[i] = random.choice(wordlist)
			
	return(tempchild)


def hillclimb(start_state,goal_state):

	reached = False

	cur_state = copy.deepcopy(start_state)

	i = 0

	while(not reached):
	
		print("Curent : " + "".join(cur_state))
		print("Goal " + "".join(goal_state))
		print("Iteration : " + str(i))
		
		heuristic_value = heuristic(cur_state,goal_state)
	
		print("Heuristic value : " + str(heuristic_value))
	
		if(heuristic_value == 0):
		
			reached = True
			break
			
		tempchild = createchild(cur_state,goal_state)
		print("Temp child : " + "".join(tempchild))
		
		if(heuristic(tempchild,goal_state) < heuristic_value):
		
			cur_state = tempchild
			print('Current state updated\n')
		
		print('\n')
		i += 1	
		

start = input("Enter start string : ")

goal = input("Enter goal string (same length as start) : ")

while(len(start) != len(goal)):

	goal = input("Wrong Input.\nEnter goal string (same length as start) : ")

start_state = list(start)
goal_state = list(goal)

hillclimb(start_state,goal_state)
print('Goal state reached')
