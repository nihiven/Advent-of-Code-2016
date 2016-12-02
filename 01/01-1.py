### advent of code: 01-1
# program settings
inputFile = 'input'
token = ','

# constants
# cardinals
north = 0; south = 1; east = 2; west = 3
left = 0; right = 1

# list of direction deltas
compass = {
	north: [0,1],
	south: [0,-1],
	east: [1,0],
	west: [-1,0]
}

# orientation map
orientation = {
	north: {left: west, right: east},
	south: {left: east, right: west},
	east: {left: north, right: south},
	west: {left: south, right: north}
}

# for converting input to turn
turnTrans = {'R' :  right, 'L' :  left}

# program variables
startX = 0; x = 0
startY = 0; y = 0
direction = north

### LET'S GO
# read input
with open(inputFile) as f:
    cmdInput = f.readline().split(token)

# parse input
cmdList = []
for cmd in cmdInput:
	cmdList.append(	[cmd.strip()[0],	# first character
									cmd.strip()[1:]])	# everything except first character

# process instructions
vistedList = [{x,y}]
for step in cmdList:
	turn = turnTrans[step[0]]
	distance = step[1]
	# take a walk
	direction = orientation[direction][turn] 								# turn
	x = int(x) + int(compass[direction][0]) * int(distance)	# x
	y = int(y) + int(compass[direction][1]) * int(distance)	# y

# taxiiii!
print 'distance:', abs(startX - x) + abs(startY - y)
