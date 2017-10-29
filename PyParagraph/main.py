import os

"""
---- PyParagraph -------
In this challenge, you get to play the role of chief linguist at a local learning academy.
As chief linguist, you are responsible for assessing the complexity of various passages of writing,
ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having
read so many passages, you've since come up with a fairly simple set of metrics for assessing
complexity.Your task is to create a Python script to automate the analysis of any such passage using
these metrics. 
"""

print("\nChoose File to Analyze:\n(1)paragraph_1.txt\n(2)paragraph_2.txt\n")
file_select = input("Enter selection : ")

#create filepath
if file_select == "1":
    filepath = os.path.join("raw_data","paragraph_1.txt")
elif file_select == "2":
    filepath = os.path.join("raw_data","paragraph_2.txt")
else:
    print("Not a valid selection")
    exit()

#init variables
sentences_list = []
total_words = 0
total_letters = 0
avg_letter_len = []
avg_sentence_len = []

#open file for reading
with open(filepath, 'r') as text:

    #read contents as a string
    contents = text.read()

    #split contents into sentences
    sentences_list = contents.split(".")

    #split() creates an extra blank list item at the end. Remove this
    sentences_list.pop()

    #collect data for each sentence
    for sentence in sentences_list:

        #split sentences into words
        word_list = []
        word_list = sentence.split(" ")
        #remove white-spaces from the list
        word_list = list(filter(None, word_list))

        #get total words
        total_words = total_words + len(word_list)

        #add up letters for the sentence
        for word in word_list:
            total_letters = total_letters + len(word)

        #get average word count for a sentence
        avg_sentence_len.append(len(word_list))
        
    print(f"\nParagraph Analysis ({filepath})")
    print("-------------------")

    print(f"Approximate Word Count: {total_words}")
    print(f"Approximate Sentence Count: {len(sentences_list)}")
    print(f"Average Letter Count: {total_letters/total_words}")
    print(f"Average Sentence Length: {sum(avg_sentence_len)/len(sentences_list)}\n")
