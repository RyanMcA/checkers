'''
The way this game is played is the board is printed, then the AI will go.
You play the 'b' pieces and the computer plays the 'a' pieces
enter the location of the piece given the coordinate system on the board
enter each step, including the location of any piece you will take

'''
import random
#'''
board = [['a', 0 ,'a', 0 ,'a', 0 ,'a', 0 ,0],
		 [ 0 ,'a', 0 ,'a', 0 ,'a', 0 ,'a',1],
		 ['a', 0 ,'a', 0 ,'a', 0 ,'a', 0 ,2],
		 [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,3],
		 [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,4],
		 [ 0 ,'b', 0 ,'b', 0 ,'b', 0 ,'b',5],
		 ['b', 0 ,'b', 0 ,'b', 0 ,'b', 0 ,6],
		 [ 0 ,'b', 0 ,'b', 0 ,'b', 0 ,'b',7],
		 [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 ,100]]
'''
#			#0	#1	#2	#3	#4	#5	#6	#7
board =  [['a', 0 ,'a', 0 ,'a', 0 ,'a', 0 ,100], #0
		  [ 0 ,'a', 0 ,'a', 0 , 0 , 0 , 0 ,100], #1
		  ['a', 0 ,'a', 0 , 0 , 0 ,'b', 0 ,100], #2
		  [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,100], #3
		  [ 0 , 0 ,'b', 0 ,'b', 0 ,'b', 0 ,100], #4
		  [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,100], #5
		  [ 0 , 0 , 0 , 0 ,'b', 0 ,'b', 0 ,100], #6
		  [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,100], #7
		  [100,100,100,100,100,100,100,100,100]]
'''#'''
realboard=board
pieceAN,pieceAK,pieceBN,pieceBK=[],[],[],[]
options=[]
moveOption={}
moveOptions=[]
moveOptionNum={}
nottakelist=[]
path=[]
port=0
'''#'''
def printboard():
	a=0
	print "      A   B   C   D   E   F   G   H"
	for y in realboard:
		print '    |---|---|---|---|---|---|---|---|'
		print "#",a,
		for x in y:
			print '|',
			if x!=0:
				print x,
			else:
				print ' ',
		print '#'
		a+=1
def loss():
	brdUP()
	lossA=False
	lossB=False
	
	if pieceAN==pieceAK==[]:
		lossA=True
	if pieceBN==pieceBK==[]:
		lossB=True
	if lossA==True:
		print "CPU WINS!"
		return True
	if lossB==True:
		print "HUMAN WINS!"
		return True
	else:
		return False
def brdUP():
	printboard()
#	if pieceAN:
	del pieceAN[:]
#	if pieceAK:
	del pieceAK[:]
#	if pieceBN:
	del pieceBN[:]
#	if pieceBK:
	del pieceBK[:]
	y=0
	for Y in board:
		x=0
		for X in Y:
			if X=='a':
				pieceAN.append((y,x))
			elif X=='A': 
				pieceAK.append((y,x))
			elif X=='b':
				pieceBN.append((y,x))
			elif X=='B':
				pieceBK.append((y,x))
			x+=1
		y+=1
	return pieceAN,pieceAK,pieceBN,pieceBK
'''#'''
def canMove(y,x,piece):
	if board[y+1][x+1]==0:
		nottakelist.append([[y,x],[y+1,x+1]])
	if board[y+1][x-1]==0:
		nottakelist.append([[y,x],[y+1,x-1]])
	if board[y-1][x+1]==0 and piece=='A':
		nottakelist.append([[y,x],[y-1,x+1]])
	if board[y-1][x-1]==0 and piece=='A':
		nottakelist.append([[y,x],[y-1,x-1]])
def cantake(y,x,opponent):
	if ((board[y+1][x+1] in opponent) and board[y+2][x+2]==0)or((board[y-1][x+1] in opponent) and board[y-2][x+2]==0)or((board[y+1][x-1] in opponent) and board[y+2][x-2]==0)or((board[y-1][x-1] in opponent) and board[y-2][x-2]==0):
		return True
	else:
		return False
def canTake2(y,x,opponent,dir,piece):
	#print y,x,opponent,dir,piece
	if (board[y+1][x+1] in opponent) and board[y+2][x+2]==0 and dir==1:
		horiz=1#horiz
		vert=1#vert
		return vert,horiz
	elif (board[y-1][x+1] in opponent) and board[y-2][x+2]==0 and dir==2:
		horiz=1#horiz
		vert=-1#vert
		return vert,horiz
	elif (board[y+1][x-1] in opponent) and board[y+2][x-2]==0 and dir==3:
		horiz=-1#horiz
		vert=1#vert
		return vert,horiz
	elif (board[y-1][x-1] in opponent) and board[y-2][x-2]==0 and dir==4:
		horiz=-1#horiz
		vert=-1#vert
		return vert,horiz
def take(y,x,vert,horiz,opponent):
	piece=board[y][x]
	board[y][x],board[y+vert][x+horiz]=0,0
	y=y+vert
	x=x+horiz
	path.append([y,x])
	y=y+vert
	x=x+horiz
	path.append([y,x])
	p=1
	if y==7:
		piece='A'
	while p<=4:
		if canTake2(y,x,opponent,p,piece) and (piece=='A' or p==1 or p==3):
			(vert,horiz)=canTake2(y,x,opponent,p,piece)
			take(y,x,vert,horiz,opponent)
		else:
			options.append(path[:])
		p+=1
	if path:
		del path[-1]
		del path[-1]
'''def take2(y,x,opponent):
	if board[y][x]=='A' or board[y][x]=='B':
		if (board[y+1][x+1] in opponent) and board[y+2][x+2]==0:
			print '+1,+1'
			take(y,x,1,1)
			del path[-2:0]
		elif (board[y-1][x+1] in opponent) and board[y-2][x+2]==0:
			print '+1,-1'
			take(y,x,1,-1)
			del path[-2:0]
		elif (board[y+1][x-1] in opponent) and board[y+2][x-2]==0:
			print '-1,+1'
			take(y,x,-1,1)
			del path[-2:0]
		elif (board[y-1][x-1] in opponent) and board[y-2][x-2]==0:
			print '-1,-1'
			take(y,x,-1,-1)
			del path[-2:0]
	elif board[y][x]=='a':
		if (board[y+1][x+1] in opponent) and board[y+2][x+2]==0:
			take(y,x,1,1)
			del path[-2:0]
		elif (board[y+1][x-1] in opponent) and board[y+2][x-2]==0:
			take(y,x,-1,1)
			del path[-2:0]
	elif board[y][x]=='b':
		if (board[y-1][x+1] in opponent) and board[y-2][x+2]==0:
			take(y,x,1,-1)
			del path[-2:0]
		elif (board[y-1][x-1] in opponent) and board[y-2][x-2]==0:
			take(y,x,-1,-1)
			del path[-2:0]
'''#'''
def turnA():
	#brdUP()
	opponent=['b','B']
	piece = 'A'
	for p in pieceAN:
	#	print 1
		del path[:]
		(y,x)=p
		if canTake2(y,x,opponent,1,piece) or canTake2(y,x,opponent,3,piece):
			if canTake2(y,x,opponent,1,piece):
				path.append([y,x])
				(vert,horiz)=canTake2(y,x,opponent,1,piece)
				take(y,x,vert,horiz,opponent)
			if canTake2(y,x,opponent,3,piece):
				path.append([y,x])
				(vert,horiz)=canTake2(y,x,opponent,3,piece)
				take(y,x,vert,horiz,opponent)			
			board=realboard
		else:
			canMove(y,x,'a')
	a=0
	for e in options:
		moveOptions.append(len(e))
	#	print moveOptions[a]
		moveOptionNum[len(e)]=e
		a+=1
	if moveOptions:
		normalmax=max(moveOptions)
	for i in pieceAK:
	#	print 1
		del path[:]
		(y,x)=i
		if cantake(y,x,opponent):
			a=1
			while a<=4:
				#board=realboard
				if canTake2(y,x,opponent,a,piece):
					path.append([y,x])
					(vert,horiz)=canTake2(y,x,opponent,a,piece)
					take(y,x,vert,horiz,opponent)
				a+=1
			board=realboard
		else:
			canMove(y,x,'A')
	#print nottakelist
	if moveOptions:
		allmax=max(moveOptions)
		
	if not moveOptions:
		moving = random.choice(nottakelist)
		[y,x]=moving[0]
		piece=realboard[y][x]
		realboard[y][x]=0
		[y,x]=moving[1]
		realboard[y][x]=piece
	else:
		if normalmax==allmax:
			piece='a'
			#print 'aaaaaaaa'
		else:
			piece='A'
			#print 'A'
		a=0
		for e in options:
			moveOptions.append(len(e))
			#print moveOptions[a]
			moveOptionNum[len(e)]=e
			a+=1
		maxx = max(moveOptions)
		#print 'max', maxx
		#print moveOptionNum[maxx]
		takePath = moveOptionNum[maxx]
		(y,x)=takePath[0]
		#print piece
		for xy in takePath:
			(y,x)=xy
			if y==7:
				piece='A'
			realboard[y][x]=0
		#print piece
	realboard[y][x]=piece
	#print realboard[y][x],y,x
A,B,C,D,E,F,G,H=0,1,2,3,4,5,6,7
def turnB():
	#brdUP()
	del path[:]
	piece = 0
	while piece!='b' and piece!='B':
		print 'invalid'
		(x,y)=input("piece location (x,y):")
		piece=realboard[y][x]
	path.append([y,x])
	while raw_input("end?y/n")=='n':
		(x,y)=input("next spot on path (x,y):")
		path.append([y,x])
	for i in path:
		(y,x)=i
		realboard[y][x]=0
		if y==0:
			piece='B'
	realboard[y][x]=piece
	#brdUP()	

def playgame():
	while not loss():
		turnA()
		if not loss():
			turnB()
#playgame()
#turnA()
def takemove(y,x,y1,x1):
	taken=realboard[(y1+y)/2][(x1+x)/2]
	if taken=='a' or taken=='A':
		return True
def turnb(x,y):
	movedone=False
	if x==-1 and y==-1:
		(x,y)=input("piece location (x,y):")
		piece = realboard[y][x]
		while piece!='b' and piece!='B':
			print 'Invalid'
			(x,y)=input("piece location (x,y):")
			piece = realboard[y][x]
		if raw_input('y/n')==y:
			piece=realboard[y][x]
		else:
			turnb(-1,-1)
	else:
		piece=realboard[y][x]
	x1,y1=x,y
	(x,y)=input("move to (x,y):")
	if (x==x1+1 or x==x1-1) and (y==y1+1 or y==y1-1):
		movedone=True
		realboard[y1][x1]=0
		realboard[y][x]=piece
	elif takemove(y,x,y1,x1) and (x==x1+2 or x==x1-2) and (y==y1+2 or y==y1-2):
		movedone=False
		realboard[y1][x1]=0
		realboard[(y1+y)/2][(x1+x)/2]=0
		realboard[y][x]=piece
	elif x==100 and y==100:
		movedone=True
	else:
		print "---INVALID---"
		turnb(x1,y1)
	if not movedone:
		turnb(x,y)
printboard()
turnb(-1,-1)