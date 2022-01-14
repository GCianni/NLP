# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import nltk
#nltk.download('punkt')

def import_corpus(file_name):
    with open(file_name, "r", encoding="utf8") as f:
        imported_corpus= f.read()
    return imported_corpus

def word_filter(tokens_list):
    word_list = []
    for token in tokens_list:
        if token.isalpha():
            word_list.append(token)
    return word_list

def normalization(word_list):
    norm_list = []
    for word in word_list:
        norm_list.append(word.lower())
    return norm_list


## Types of Mistakes
def insert_letter(slice):
    new_words = []
    letters='abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for Left, Right in slice:
        for letter in letters:
            new_words.append(Left+letter+Right)
    return new_words

def delet_char(slice):
    new_words = []
    for left, right in slice:
        new_words.append(left+right[1:])
    return new_words

def change_letter(slice):
    new_words=[]
    letters='abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for left, right in slice:
        for letter in letters:
            new_words.append(left+letter+right[1:])
    return new_words

def swipe_chars(slice):
    new_words=[]
    for left, right in slice:
        if (len(right)>1):
            new_words.append(left+right[1]+right[0]+right[2:])
    return new_words

###
def word_generator(word):
    slice = []
    for i in range(len(word)):
        slice.append((word[:i], word[i:]))
    generated_words = insert_letter(slice)
    generated_words += delet_char(slice)
    generated_words += change_letter(slice)
    generated_words += swipe_chars(slice)
    return generated_words

def probability(generated_words):
    return frequency[generated_words] / len(norm_list)

def spell_checker(word):
    generated_words = word_generator(word)
    correct_word = max(generated_words,key=probability)
    return correct_word

### AVALIATION OF CHECKS
def create_test_data(file_name):
    test_word_list=[]
    f=open(file_name,'r', encoding = 'utf-8')
    for linha in f:
        right, wrong = linha.split()
        test_word_list.append((right,wrong))
    f.close()
    return test_word_list

def avaliation (test, vocabulary) :
    word_number=len(test);
    got_right=0
    unknown_word = 0
    for right, wrong in test:
        corrected_word = spell_checker(wrong)
        if corrected_word == right:
            got_right += 1;
        else:
            unknown_word += (corrected_word not in vocabulary)
    accuracy_rate=round(got_right*100/word_number,2)
    unknowing_rate=round(unknown_word*100/word_number, 2)
    print(f'{accuracy_rate}% of {word_number} words, unknown words is {unknowing_rate}%')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    corpus = import_corpus('artigos.txt')

    tokens = nltk.tokenize.word_tokenize(corpus)
    total_words = word_filter(tokens)
    # print(f"Number of words in the corpus is {len(total_words)}")

    norm_list = normalization(total_words)
    #print(len(set(norm_list)))

    #CORRIGIR ISSO DPS
    palavra_exemplo = "lgica"
    palavras_geradas = word_generator(palavra_exemplo)
    #print(palavras_geradas)

    frequency = nltk.FreqDist(norm_list)

    test_dataset = create_test_data('palavras.txt')

    vocabulay = set(norm_list)
    avaliation(test_dataset, vocabulay)
