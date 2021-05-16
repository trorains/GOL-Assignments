def reverseSentence(lst):
    word = ""
    for letter in lst:
        word += letter
    
    word_split= word.split()
    word_reversed = word_split[:: -1]
    final_list = []
    for letter in word_reversed:
        characters = list(letter)
        final_list.append(characters)

    return  final_list
    


A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
print(reverseSentence(A))