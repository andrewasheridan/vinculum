"""Emoji Utilities."""
__all__ = ["number_to_emoji"]
from collections.abc import Iterator

from typing_extensions import Final

from vinculum_api.lib._emojis import EMOJIS

BASE: Final[int] = len(EMOJIS)  # 887


def _number_to_base_digits(number: int, /, *, base: int) -> Iterator[int]:
    """Get the base-10 number as digits in a new base."""
    if number == 0:
        return reversed([0])

    digits: list[int] = []
    while number:
        digits.append(int(number % base))
        number //= base

    return reversed(digits)


def _get_emoji(indexes: Iterator[int], /) -> str:
    return "".join(EMOJIS[i] for i in indexes)


def number_to_emoji(number: int, /) -> str:
    """Get an emoji for the given number."""
    digits = _number_to_base_digits(number, base=len(EMOJIS))
    return _get_emoji(digits)
