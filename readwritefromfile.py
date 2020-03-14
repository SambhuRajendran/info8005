filepath= 'S:\\INFO8005_PY\\'
filetoread = 'Lab1-Task2.txt'
filetowrite = '\write_\out.txt'

readfile = open(filepath + filetoread, "r")
linedata =  readfile.read()
print(linedata)
print(linedata[1:100])

writtenfile = open(filepath + filetowrite, "w")
writtenfile.write("Please exit the world, Corona")

