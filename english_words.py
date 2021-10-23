'''Creates a list with 3000 most commmon English words'''

source_file = open("english_words.txt", "r+")

words = []
for line in source_file:
  words.append(line.strip("\n"))
  

source_file.close()



