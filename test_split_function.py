import pytest
from split_function import split_function

test1 = "Hello,world."
test2 = "Apples Pears Oranges"
test3 = "That new episode of House of the Dragon was pretty good."
test4 = ""
test5 = "Greetings."
test6 = "***H***E***L***L***O***"


def test_split_function():
    assert split_function(test1, ",") == ["Hello", "world."]
    assert split_function(test2, " ") == ["Apples", "Pears", "Oranges"]
    assert split_function(test3, "&D*@") == ["That new episode of House of the Dragon was pretty good."]
    assert split_function(test4, "!") == [""]
    assert split_function(test5, test5) == ["", ""]
    assert split_function(test6, "***") == ["", "H", "E", "L", "L", "O", ""]

    with pytest.raises(ValueError):
        assert split_function(test1, "") == ValueError
