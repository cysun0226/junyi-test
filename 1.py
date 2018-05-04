

numbers = [1, [12, 3, [4, [5, 16]]]]

def reverse_sentence(sentence):
    words = sentence.split(' ')
    result_str = ''
    for w in words:
        result_str += (reverse_str(w)+' ')
    return result_str


def reverse_str(str):
    return str[::-1]



str = input('\n1. Please input a string: ')
print('\n> reverse string: ' + reverse_str(str))

sentence = input('\n2. Please input a sentence: ')
print('\n> reverse sentence: ' + reverse_sentence(sentence))
