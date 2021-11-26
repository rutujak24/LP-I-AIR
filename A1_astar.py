import copy

class StateObject:

	def __init__(self,arr,g):
	
		self.arr = copy.deepcopy(arr)
		self.g = g
		self.h = 0
		self.f = self.g + self.h
		
	def isEqual(self,obj):
	
		for i in range(3):
			for j in range(3):
				if(self.arr[i][j] != obj.arr[i][j]):
				
					return(False)
					
		return(True)
				
				
	def findh(self,goal):
	
		diff = 0
		
		for i in range(3):
			for j in range(3):
				if(self.arr[i][j] != goal.arr[i][j]):
					diff += 1
					
		self.h = diff
		self.f = self.g + self.h
		
def read_array():

	arr = []
	
	for i in range(3):
	
		arr.append(list(map(int,input().split())))
		
	return(arr)
	
	
def findbest(openlist):

	index = 0

	minf = openlist[0].f
	
	for i in range(1,len(openlist)):
	
		if(openlist[i].f < minf):
		
			index = i
			minf = openlist[i].f
		
	return(index)			


def isPresent(openlist,obj):

	for i in range(len(openlist)):
	
		if(obj.isEqual(openlist[i])):
		
			return(i)

	return(-1)

def addchild(openlist,parent,goal):

	x = -1
	y = -1
	
	for i in range(3):
		for j in range(3):
		
			if(parent.arr[i][j] == 0):
			
				x = i
				y = j
				break	
				
	temparr1 = copy.deepcopy(parent.arr)
	temparr2 = copy.deepcopy(parent.arr)
	temparr3 = copy.deepcopy(parent.arr)
	temparr4 = copy.deepcopy(parent.arr)
	
	templist = []
	
	if(x-1 >= 0):
		temparr1[x][y],temparr1[x-1][y] = temparr1[x-1][y],temparr1[x][y]
		tempobj = StateObject(temparr1,parent.g+1)
		tempobj.findh(goal)
		templist.append(tempobj)
	
	if(x+1 < 3):
		temparr2[x][y],temparr2[x+1][y] = temparr2[x+1][y],temparr2[x][y]
		tempobj = StateObject(temparr2,parent.g+1)
		tempobj.findh(goal)
		templist.append(tempobj)
		
	if(y-1 >= 0):
		temparr3[x][y],temparr3[x][y-1] = temparr3[x][y-1],temparr3[x][y]
		tempobj = StateObject(temparr3,parent.g+1)
		tempobj.findh(goal)
		templist.append(tempobj)
		
	if(y+1 < 3):
		temparr4[x][y],temparr4[x][y+1] = temparr4[x][y+1],temparr4[x][y]
		tempobj = StateObject(temparr4,parent.g+1)
		tempobj.findh(goal)
		templist.append(tempobj)


	for tempobj in templist:
	
		index = isPresent(openlist,tempobj)
		
		if(index == -1):
			openlist.append(tempobj)
		
		else:
			if(tempobj.f < openlist[index].f):
				openlist[index].f = tempobj.f
				openlist[index].g = tempobj.g
				openlist[index].h = tempobj.h	
			


def astar(start,goal):

	openlist = [start]
	closelist = []
	
	moves = 0
	
	found = False
	
	while(len(openlist) != 0):
	
		moves += 1
	
		cbi = findbest(openlist)
		cb = openlist[cbi]
		closelist.append(cb)
		del openlist[cbi]
		
		if(cb.isEqual(goal)):
		
			print(cb.arr)
			print(cb.g)
			print(cb.h)
			found = True
			break
	
		print(cb.arr)
		print(cb.g)
		print(cb.h)
	
		addchild(openlist,cb,goal)
			
		if(moves > 20):
		
			break	
			
	if(not found):
		moves = -1
		
	return(moves)

#main


print("Enter start state : ")	
start = StateObject(read_array(),0)

print("Enter goal state : ")
goal = 	StateObject(read_array(),-1)

start.findh(goal)

moves = 0

if(start.isEqual(goal)):

	print("Goal state reached\nMoves required : {0}".format(moves))
	
else:

	moves = astar(start,goal)
	
	if(moves != -1):
	
		print("Goal state reached\nMoves required : {0}".format(moves))
		
	else:
	
		print("Goal state cannot be reached\n")
