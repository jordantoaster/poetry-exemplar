from poetry_exemplar.add_one import add_one

def test_add_one():
    result = add_one(1)
    assert result == 2
