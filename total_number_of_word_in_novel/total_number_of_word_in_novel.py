
import re 
# List of novels txt file name
novels = ['sons_and_lovers_lawrence.txt',
          'metamorphosis_kafka.txt',
          'the_way_of_all_flash_butler.txt',
          'robinson_crusoe_defoe.txt',
          'to_the_lighthouse_woolf.txt',
          'james_joyce_ulysses.txt',
          'moby_dick_melville.txt']

#List to store all words of different novel
words_of_novel =[]

#list to store number of unique word in novels
unique_words_of_novel = []

#Loop to remove all (special char , white space , digits) and to store in list
for novel in novels:
    file = open(novel,'r',encoding="utf8")
    read_novel = file.read()
    start_reading = re.search(r'START OF',read_novel)
    #start counting words after this line
    startindex = read_novel.find('\n',start_reading.end())
    end_reading = re.search(r'END OF',read_novel)
    read_novel = read_novel[startindex:end_reading.start()]
    read_novel= re.sub("[^a-zA-Z]"," ",read_novel)
    #for removing extra space from read_novel
    words_of_novel.append(read_novel.strip().split())
    unique_words_of_novel.append(len(set(read_novel.strip().split())))
    
#finding index of bext novel with max unique word
index = unique_words_of_novel.index(max(unique_words_of_novel))
best = words_of_novel[index]
x=set(best)
y=set(best)

#To remove all the words in best novel which are comman in other novels
for novel in words_of_novel:
    if best!=novel:
        x=set(x)-set(novel)
    #To store all comman words from all novels
    y = set(y)&set(novel)
# Storing All unique words in text file
file = open("unique_word_in_best_novel.txt",'w')
file.write(str(x))
#Here is your Best novel
print ("\n\nBest novel is",novels[index] ,"with :-")
print ("Total words :-",len(words_of_novel[index]))
print ("Unique Words:-",unique_words_of_novel[index])
print ("Unique Words in this novel form all:-",len(x))
print ("Total Comman Words in All Novel :-",len(y))
