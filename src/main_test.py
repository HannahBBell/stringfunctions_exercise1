def capitalise_string(s):
    return s.upper()

def test_capitalise_string():
    assert capitalise_string("hello") == "hello".upper()

def test_capitalise_string():
    assert capitalise_string("hello world") == "hello world".upper()
