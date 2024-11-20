import pytest
from main import prefix_to_infix

def test_prefix_to_infix():

    # Тесты для корректных выражений
    assert prefix_to_infix("+ 1 2") == "(1 + 2)"
    assert prefix_to_infix("- + 1 2 3") == "((1 + 2) - 3)"
    assert prefix_to_infix("* + 1 2 3") == "((1 + 2) * 3)"
    assert prefix_to_infix("/ - 10 2 5") == "((10 - 2) / 5)"
    assert prefix_to_infix("+ - 7 5 * 2 3") == "((7 - 5) + (2 * 3))"

    # Тесты для некорректных символов в выражении
    assert prefix_to_infix("1 & 2") == "1 & 2"
    assert prefix_to_infix("* + 1 2 @") == "* + 1 2 @"

    # Тесты с одним операндом
    assert prefix_to_infix("- 5") == "- 5"
    assert prefix_to_infix("+ 4") == "4"

    # Тест с пустым выражением
    assert prefix_to_infix("") == ""

    # Тест с числовыми значениями без пробелов
    assert prefix_to_infix("400 200 -") == "400 200 -"

if __name__=="__main__":
    pytest.main()
