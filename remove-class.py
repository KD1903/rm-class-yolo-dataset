import os

#loop through all three folders
for i in ['train', 'test', 'valid']:
    #list all the files insode  folder
    for f in os.listdir(os.path.join(i, 'labels')):
        print(os.path.join(i, 'labels', f))

        #open and real all lines of file
        with open(os.path.join(i, 'labels', f), 'r+') as lf:
            data = lf.readlines()

            #loop through all lines insode file
            for l in data:
                #check if lable is 1, remove that line
                if l.startswith('1'):
                    data.remove(l)
            
            #truncate file data and save updated lisrt in file
            lf.seek(0)
            lf.truncate()
            lf.write('\n'.join(data))
