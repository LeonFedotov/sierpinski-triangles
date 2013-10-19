def drawSerp(dept = 10, drawChar = ".", lastLine = []):
	if dept:
		newLine = []
		for x in xrange(len(lastLine)+1):
			if x == 0 or x == len(lastLine) :
				newLine.append(1)
			else :
				newLine.append(lastLine[x-1]+lastLine[x])
		print "%s".rjust((dept+1)*len(drawChar)) % (" "*len(drawChar)).join(map(lambda x: drawChar if x%2 else " "*len(drawChar),newLine))

		drawSerp(dept-1, drawChar, newLine)