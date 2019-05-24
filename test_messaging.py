import pytest
from messaging import process_intent, build_message

def test_with_capitalization():
    intent = process_intent("NB")
    assert intent == "n"

def test_with_whitespace():
    intent = process_intent(" south  ")
    assert intent == "s"

def test_with_specialchars():
    intent = process_intent("I'm heading to work!!!")
    assert intent == "n"

def test_error():
    intent = process_intent("idk")
    assert intent == "error"

def test_no_time_savings():
    msg = build_message("n", "0", "$3.00")
    assert msg == "Don't take the toll, it won't save you any time and will cost you $3.00."


def test_home():
    msg = build_message("s", "1", "$3.00")
    assert msg == "Toll rate to get back home is $3.00 and will save you 1 minute."


def test_work():
    msg = build_message("n", "2", "$3.00")
    assert msg == "Toll rate to get to work is $3.00 and will save you 2 minutes."