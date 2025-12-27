import pytest

from app.logic import (
    is_palindrome,
    fibonacci,
    count_vowels,
    calculate_discount,
    flatten_list,
    word_frequencies,
    is_prime,
)


class TestIsPalindrome:
    @pytest.mark.parametrize(
        "text, expected",
        [
            ("kajak", True),
            ("Kobyła ma mały bok", True),
            ("python", False),
            ("", True),
            ("A", True),
        ],
    )
    def test_is_palindrome(self, text, expected):
        assert is_palindrome(text) is expected


class TestFibonacci:
    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 0),
            (1, 1),
            (5, 5),
            (10, 55),
        ],
    )
    def test_fibonacci_values(self, n, expected):
        assert fibonacci(n) == expected

    def test_fibonacci_negative_raises(self):
        with pytest.raises(ValueError):
            fibonacci(-1)


class TestCountVowels:
    @pytest.mark.parametrize(
        "text, expected",
        [
            ("Python", 2),
            ("AEIOUY", 6),
            ("bcd", 0),
            ("", 0),
            ("Próba żółwia", 3),  # patrz uwaga poniżej
        ],
    )
    def test_count_vowels(self, text, expected):
        assert count_vowels(text) == expected


class TestCalculateDiscount:
    @pytest.mark.parametrize(
        "price, discount, expected",
        [
            (100, 0.2, 80.0),
            (50, 0, 50.0),
            (200, 1, 0.0),
        ],
    )
    def test_calculate_discount_ok(self, price, discount, expected):
        assert calculate_discount(price, discount) == expected

    @pytest.mark.parametrize("discount", [-0.1, 1.5])
    def test_calculate_discount_invalid_discount_raises(self, discount):
        with pytest.raises(ValueError):
            calculate_discount(100, discount)


class TestFlattenList:
    @pytest.mark.parametrize(
        "nested, expected",
        [
            ([1, 2, 3], [1, 2, 3]),
            ([1, [2, 3], [4, [5]]], [1, 2, 3, 4, 5]),
            ([], []),
            ([[[1]]], [1]),
            ([1, [2, [3, [4]]]], [1, 2, 3, 4]),
        ],
    )
    def test_flatten_list(self, nested, expected):
        assert flatten_list(nested) == expected


class TestWordFrequencies:
    def test_to_be_or_not(self):
        assert word_frequencies("To be or not to be") == {
            "to": 2,
            "be": 2,
            "or": 1,
            "not": 1,
        }

    def test_hello_hello(self):
        assert word_frequencies("Hello, hello!") == {"hello": 2}

    def test_empty(self):
        assert word_frequencies("") == {}

    def test_python_repeated(self):
        assert word_frequencies("Python Python python") == {"python": 3}

    def test_punctuation_ignored(self):
        result = word_frequencies("Ala ma kota, a kot ma Ale.")
        # najważniejsze: interpunkcja ignorowana i case-insensitive
        assert result.get("ala", 0) == 1
        assert result.get("ma", 0) == 2
        assert result.get("kota", 0) == 1
        assert result.get("a", 0) == 1
        assert result.get("kot", 0) == 1
        assert result.get("ale", 0) == 1


class TestIsPrime:
    @pytest.mark.parametrize(
        "n, expected",
        [
            (2, True),
            (3, True),
            (4, False),
            (0, False),
            (1, False),
            (5, True),
            (97, True),
        ],
    )
    def test_is_prime(self, n, expected):
        assert is_prime(n) is expected
