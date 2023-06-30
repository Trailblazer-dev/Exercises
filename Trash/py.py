file = open("word.txt", "r")#when you "w" in text will already having a text you will overwrite displacing the original text like what I have done
print(file.read())#But if you want to add information use "a"
file = open("word.txt", "w")
file.write("But am like a  Shark I don't go back if I left you just remain in the past stop trying to resurface with hopes")
file.close()
file = open("word.txt", "r")
print(file.read())
#to delete a file like the above word.txt we use import as shown below
import os
os.remove("word.txt")