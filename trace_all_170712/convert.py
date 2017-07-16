import sys

infname = sys.argv[1]
outfname = sys.argv[1] + ".reverse"

info = open(sys.argv[1], "r")
outfo = open(sys.argv[1] + ".reverse", "w")


lines = info.readlines()

for i in reversed(range(len(lines))):
	outfo.write(lines[i])

#####
from subprocess import call
call(["cat", outfname])


