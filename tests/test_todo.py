# File: tests/test_todo.py

import pytest
from lib.todo import todo


true_file = "notes/notes_todo.txt"
false_file = "notes/notes_random.txt"

def test_true_case():
    result = todo("#TODO", true_file)
    assert result == True 

def test_false_case():
    result = todo("#TODO", false_file)
    assert result == False

