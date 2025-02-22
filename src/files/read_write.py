wf = open("myfile.txt", 'w')
contents = str()
wf.write(contents)

while 'end'  not in contents:
    contents = input("Enter text to write into file,end to quit in sentence ")
    if 'end' not in contents:
        wf.write(contents+"\n")
wf.close()


rf = open("myfile.txt", 'r')
print(len(rf.read().split('\n')))
rf.close()