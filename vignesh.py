import googletrans
from googletrans import Translator
translator=Translator()
source=open('C:\Users\GOD\Downloads\find_words.txt', "r")
print(source.read())
result = translator.translate(source,src='en',dest='fr')
print(result.dest)
p=result.dest
print(result.text)
f1 = p
f2 = open('C:\Users\GOD\Downloads\t8.shakespeare.txt', 'w')
for line in f1:
    f2.write(line.replace(source,f1))
f1.close()
f2.close()
