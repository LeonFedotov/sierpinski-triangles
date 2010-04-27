def drawSerp(dept = 10, drawChar = ".", lastLine = []):
	if dept:
		newLine = []
		for x in xrange(len(lastLine)+1):
			if x == 0 or x == len(lastLine) :
				newLine.append(1)
			else :
				newLine.append(lastLine[x-1]+lastLine[x])
				
		udrawChar = "".join([" " for j in xrange(len(drawChar))])
		wholeLine = udrawChar.join([(lambda a: a%2)(i) and drawChar or udrawChar for i in newLine])
		print "%s".rjust((dept+len(lastLine)-len(newLine)+2)*len(drawChar)) % wholeLine
		drawSerp(dept-1, drawChar, newLine)