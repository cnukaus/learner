# simple script to add alias to NVL() function
f1=open("sql.txt","r")
lines=f1.readlines()

for line in lines:
	if "NVL" in line:
		print(line.replace("\n", "")+" as "+line[line.find(".")+1:line.strip()[1:].find(",")+2])#print(line+" "+line[line.find("."),line.find(",")-1])
	else:
		print(line)
