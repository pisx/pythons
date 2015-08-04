
	
for i in range(1,10):
	for j in range(1,i+1):
		print('%d * %d = %-3d' % (i,j,i*j),end='')
		j = j + 1
	print()
	

#i = 1
#j = 1
#while i < 10:
#	while j <= i:
#		print('%d * %d = %-3d' % (i,j,i*j),end='')
#		j = j + 1
#	print()
#	j = 1
#	i = i + 1