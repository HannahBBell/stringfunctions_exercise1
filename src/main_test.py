def capitalise_string(s):
    return s.upper()

def test_capitalise_string():
    assert capitalise_string("hello") == "hello".upper()

def test_capitalise_string():
    assert capitalise_string("hello world") == "hello world".upper()

def test_capitalise_string():
    assert capitalise_string("hello world 2") == "hello world 2".upper()

def decapitalise_string(st):
    return s.lower()

def test_decapitalise_string():
    assert decapitalise_string("HELLO, WORLD1") == "hello, world1"