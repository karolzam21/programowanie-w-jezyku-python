import re
import string


def is_palindrome(text: str) -> bool:
    normalized = "".join(ch.lower() for ch in text if not ch.isspace())
    return normalized == normalized[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    vowels = set("aeiouyAEIOUY")
    return sum(1 for ch in text if ch in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("musi mieścić się w przedziale 0..1")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def word_frequencies(text: str) -> dict:
    # usuwamy interpunkcję, małe litery
    cleaned = re.sub(rf"[{re.escape(string.punctuation)}]", " ", text.lower())
    words = cleaned.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
