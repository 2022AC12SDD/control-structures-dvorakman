import pytest
import helpers as h

def test_ultimate_answer():
    question1 = 'What is the meaning of Life, The Universe, Everything?'
    assert h.ultimate_answer(question1) == '42'
    question2 = 'What is 6 x 7'
    assert h.ultimate_answer(question2) == 'That is not much of a question'

def test_check_guess_bin():
    try:
        guess = 1
        target = 3
        assert(h.check_guess_bin(guess, target)) == False
        guess = 2
        target = 2
        assert(h.check_guess_bin(guess, target)) == True
    except AssertionError:
        print("check_guess_bin(guess, target) is not working expectedly")

def test_check_guess_multi():
    try:
    expect AssertionError:
        print("check_guess_multi(guess, target) is not working expectedly")