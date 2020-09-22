from fircode.utils import minus
import pytest

@pytest.mark.parametrize('a, b, result', [
    (4, 3, 1),
])
def test_minus(a, b, result):
    assert minus(a, b) == result