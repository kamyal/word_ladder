#!/bin/python3


def word_ladder(start_word, end_word, words):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony',
    'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    stack = []
    stack.append(start_word)
    queue = []
    queue.append(stack)

    file_read = open('words5.dict', 'r')
    words = file_read.readlines()

    while len(queue) != 0:
        found = False
        stack = queue.pop(0)
        a = stack[len(stack) - 1]
        for w in words:
            b = w.rstrip("\n")
            if _adjacent(a, b):
                found = True
                if b == end_word:
                    stack.insert(len(stack), end_word)
                    break
                else:
                    stack = stack.copy()
                    stack.insert(len(stack), b)
                    a = b
                    words.remove(w)
        if (found and b != end_word):
            queue.insert(0, stack)
    return stack


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder['stone', 'shone', 'phony'])
    False

    step 1- compare the first element to the other three
    step 2- if it is adjacent to the rest, return True
    step 3- if it is not adjacent to the rest, return False
    '''
    check = []
    for i in (range(len(ladder))):
        compare = (_adjacent(ladder[i], ladder[i+1]))
        check.append(compare)
        i += 1
        if i == (len(ladder)-1):
            return (all(check))


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    difference = 0
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        if word1[i] != word2[i]:
            difference += 1
    if difference == 1:
        return True
    else:
        return False


file_read = open('words5.dict', 'r')
words = file_read.readlines()
