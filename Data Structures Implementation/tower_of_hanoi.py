def move_tower(height, frompole, topole, withpole):
	if height >= 1:
		move_tower(height-1, frompole, withpole, topole)
		move_disk(frompole, topole)
		move_tower(height-1, withpole, topole, frompole)

def move_disk(frompole, topole):
	print 'Moving disk from ' + frompole + ' to ' + topole

move_tower(4, 'A', 'B', 'C')