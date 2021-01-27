#Functions

def capitalise_string(s):
    return s.upper()

def decapitalise_string(st):
    return st.lower()

def first_letter_capitalisation(word):
    return word.title()

def reverse_string(string):
    return string[::-1]


#Tests
    
def test_capitalise_string():
    assert capitalise_string("hello") == "hello".upper()

def test_capitalise_string():
    assert capitalise_string("hello world") == "hello world".upper()

def test_capitalise_string():
    assert capitalise_string("hello world 2") == "hello world 2".upper()

def test_decapitalise_string():
    assert decapitalise_string("HELLO, WORLD1") == "hello, world1"

def test_first_letter_capitalisation():
    assert first_letter_capitalisation("hello, world1") == 'Hello, World1'

def test_reverse_string():
    assert reverse_string("hello, world") == "dlrow ,olleh"
