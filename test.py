from practice import validate


def main():
    test_format()
    test_range()


def test_format():
    assert validate(r"1.2.3.4.5") == False
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False
    assert validate(r"") == False


def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.255.255.255") == False
    assert validate(r"255.512.255.255") == False
    assert validate(r"255.255.512.255") == False
    assert validate(r"255.255.255.512") == False


if __name__ == "__main__":
    main()
