#//w.a.p. to read a word then check a word  available in your file ?
word=input('Enter a word: ')
f=open('demo.txt')
data=f.read()
if word in data:
    print('your word is available')
else:
    print('your word is not available')
f.close()


#//w.a.p. to read aline then check the lines from the file then print the line only?
lineno=int(input('enter line number:'))
f=open('demo.txt')
data=f.readlines()
print(data[lineno-1])
f.close()


#//w.a.p. read a filename  from user and read the data then display the file data
filename=input('Enter filename: ')
f=open(filename)
data=f.read()
print(data)
f.close()


#//w.a.p. to read a filename if_filename is available the display file otherwise display message 'your file is not available'
filename=input('Enter filename: ')
try:
    f=open(filename)
except Exception as e:
    print('File not found')
else:
    data=f.read()
    print(data)
    f.close()


#//w.a.p. display total number of lines in your file?
f=open('demo2.py')
data=f.readlines()
print(len(data))
f.close()


#//w.a.p. read filename and line number from user then display data?
filename=input('enter the filename: ')
lineno=int(input('enter the line number: '))
f=open(filename)
data=f.readlines()
if lineno<= len(data):
  print(data[lineno-1])
else:
    print('sorry we don`t have',len(data),' that line number')
f.close()

#//w.a.p.read a word from user then check the line then the word is available then how many times available?
word=input('enter the any  word : ')
line=1
f=open('demo11.txt')
data=f.readlines()
for i in data:
    words=i.split()
    count=words.count(word)
    print('line_no-',line,count,'times')
    line=line+1
    f.close()


#//w.a.p.to read word when check the word find how many times the word occured in the file data?
word=input('enter the word: ')
f=open('demo11.py')
data=f.read()
i=data.split()
count=i.count(word)
print(count)

