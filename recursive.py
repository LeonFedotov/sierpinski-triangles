def drawSerp(dept = 10, drawChar = ".", lastLine = []):
	if dept:
		newLine = []
		for x in xrange(len(lastLine)+1):
			if x == 0 or x == len(lastLine) :
				newLine.append(1)
			else :
				newLine.append(lastLine[x-1]+lastLine[x])
		print "%s".rjust((dept+len(lastLine)-len(newLine)+2)*len(drawChar)) % (" "*len(drawChar)).join([drawChar if i%2 else (" "*len(drawChar)) for i in newLine])
		drawSerp(dept-1, drawChar, newLine) 