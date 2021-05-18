

def reverseArray(lst):
    beginning = 0
    end = len(lst)-1


    while(beginning < end):
        # temp = lst[beginning]
        # lst[beginning] = lst[end]
        # lst[end] = temp
        lst[beginning],lst[end] = lst[end],lst[beginning]
        beginning = beginning+1
        end = end -1
    return lst



def reverseArray2(lstr, starter, ender):
    length = starter - ender
    mid_point = (length//2)+starter
    for i in range(starter, mid_point):
        lstr[i],lstr[(ender-1)-i+starter]=lstr[(ender-1)-i+starter],lstr[i]

    return lstr

# def reverseSentence(lst):
#     word = ""
#     for letter in lst:
#         word += letter
    
#     word_split= word.split()
#     word_reversed = word_split[:: -1]
#     final_list = []
#     for letter in word_reversed:
#         characters = list(letter)
#         final_list.append(characters)

#     return  final_list

def reverseSentence(lst):
    sentence_backwards = reverseArray(lst)
    start = 0
    finish = 0
    len_sentence = len(sentence_backwards)
    # sentence_backwards[start],sentence_backwards[finish]
    
    while finish < len_sentence:
        while finish < len_sentence and lst[finish] != ' ':
            finish += 1
        reverseArray(lst, start, finish)
        finish += 1
        start = finish
    
    return lst

    # word = ""
    # for letter in lst:
    #     word += letter
    
    # word_split= word.split()
    # word_reversed = word_split[:: -1]
    # final_list = []
    # for letter in word_reversed:
    #     characters = list(letter)
    #     final_list.append(characters)

    # return  final_list
    


A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
print(reverseArray(A))