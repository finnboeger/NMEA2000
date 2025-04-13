from __future__ import annotations
from time import time
import math
from typing import Generic, TypeVar
from n2k.constants import *
from n2k.types import N2kBinaryStatus, N2kOnOff


def millis() -> int:
    return int(time() * 1000)


class IntRef:
    value: int

    def __init__(self, value: int = 0):
        self.value = value

    def __add__(self, other):
        if isinstance(other, IntRef):
            return self.value + other.value
        elif isinstance(other, int):
            return self.value + other
        else:
            raise TypeError(
                "unsupported operand type(s) for +: 'IntRef' and '"
                + type(other).__name__
                + "'"
            )

    def __radd__(self, other):
        if isinstance(other, IntRef):
            return other.value + self.value
        elif isinstance(other, int):
            return other + self.value
        else:
            raise TypeError(
                "unsupported operand type(s) for +: '"
                + type(other).__name__
                + "' and 'IntRef'"
            )

    def __sub__(self, other):
        if isinstance(other, IntRef):
            return self.value - other.value
        elif isinstance(other, int):
            return self.value - other
        else:
            raise TypeError(
                "unsupported operand type(s) for -: 'IntRef' and '"
                + type(other).__name__
                + "'"
            )

    def __rsub__(self, other):
        if isinstance(other, IntRef):
            return other.value - self.value
        elif isinstance(other, int):
            return other - self.value
        else:
            raise TypeError(
                "unsupported operand type(s) for +: '"
                + type(other).__name__
                + "' and 'IntRef'"
            )

    def __mult__(self, other):
        if isinstance(other, IntRef):
            return self.value * other.value
        elif isinstance(other, int):
            return self.value * other
        else:
            raise TypeError(
                "unsupported operand type(s) for *: 'IntRef' and '"
                + type(other).__name__
                + "'"
            )

    def __floordiv__(self, other):
        if isinstance(other, IntRef):
            return self.value // other.value
        elif isinstance(other, int):
            return self.value // other
        else:
            raise TypeError(
                "unsupported operand type(s) for //: 'IntRef' and '"
                + type(other).__name__
                + "'"
            )

    def __rfloordiv__(self, other):
        if isinstance(other, IntRef):
            return other.value // self.value
        elif isinstance(other, int):
            return other // self.value
        else:
            raise TypeError(
                "unsupported operand type(s) for +: '"
                + type(other).__name__
                + "' and 'IntRef'"
            )

    def __truediv__(self, other):
        if isinstance(other, IntRef):
            return self.value / other.value
        elif isinstance(other, int):
            return self.value / other
        else:
            raise TypeError(
                "unsupported operand type(s) for /: 'IntRef' and '"
                + type(other).__name__
                + "'"
            )

    def __rtruediv__(self, other):
        if isinstance(other, IntRef):
            return other.value / self.value
        elif isinstance(other, int):
            return other / self.value
        else:
            raise TypeError(
                "unsupported operand type(s) for +: '"
                + type(other).__name__
                + "' and 'IntRef'"
            )

    def __repr__(self):
        return "IntRef(" + str(self.value) + ")"

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value


def clamp_int(min_val: int, val: int, max_val: int) -> int:
    return int(min(max_val, max(min_val, val)))


def n2k_double_is_na(v: float) -> bool:
    return v == N2K_DOUBLE_NA


def n2k_float_is_na(v: float) -> bool:
    return v == N2K_FLOAT_NA


def n2k_uint8_is_na(v: float) -> bool:
    return v == N2K_UINT8_NA


def n2k_int8_is_na(v: float) -> bool:
    return v == N2K_INT8_NA


def n2k_uint16_is_na(v: float) -> bool:
    return v == N2K_UINT16_NA


def n2k_int16_is_na(v: float) -> bool:
    return v == N2K_INT16_NA


def n2k_uint32_is_na(v: float) -> bool:
    return v == N2K_UINT32_NA


def n2k_int32_is_na(v: float) -> bool:
    return v == N2K_INT32_NA


def n2k_uint64_is_na(v: float) -> bool:
    return v == N2K_UINT64_NA


def n2k_int64_is_na(v: float) -> bool:
    return v == N2K_INT64_NA


def rad_to_deg(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return math.degrees(v)


def deg_to_rad(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return math.radians(v)


def c_to_kelvin(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return v + 273.15


def kelvin_to_c(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return v - 273.15


def f_to_kelvin(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return (v - 32) * 5.0 / 9.0 + 273.15


def kelvin_to_f(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return (v - 273.15) * 9.0 / 4.0 + 32


def mbar_to_pascal(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return v * 100


def pascal_to_mbar(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return v / 1000


def hpa_to_pascal(v: float) -> float:
    return mbar_to_pascal(v)


def pascal_to_hpa(v: float) -> float:
    return pascal_to_mbar(v)


def ah_to_coulomb(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return v * 3600


def coulomb_to_ah(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return v / 3600


def hours_to_seconds(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return v * 3600


def seconds_to_hours(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return v / 3600


def meters_per_second_to_knots(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return v * 3600 / 1852


def knots_to_meters_per_second(v: float) -> float:
    if n2k_double_is_na(v):
        return v
    return v * 1852 / 3600


def n2k_reset_binary_status(_bank_status: N2kBinaryStatus) -> int:
    """
    Reset all single binary status values to not available

    This helper function returns a new fully reset 64bit bank status.
    For each individual item the status will be 3 (0b11 - Unavailable :py:class:`N2kOnOff`)
    """
    return 0xFFFFFFFFFFFFFFFF


def n2k_get_status_on_binary_status(
    bank_status: N2kBinaryStatus, item_index: int = 1
) -> N2kOnOff:
    """
    Get single status of full binary bank status returned by :py:func:`parse_n2k_binary_status`.

    :param bank_status: Full bank status read by :py:func:`parse_n2k_binary_status`
    :param item_index: Status item index 1-28
    :return: single status of full binary bank status
    """
    item_index -= 1
    if item_index > 27:
        return N2kOnOff.Unavailable

    return N2kOnOff((bank_status >> (2 * item_index)) & 0x03)


def n2k_set_status_binary_on_status(
    bank_status: N2kBinaryStatus, item_status: N2kOnOff, item_index: int = 1
) -> N2kBinaryStatus:
    """
    Set single status to full binary bank status.

    :param bank_status: Existing Bank Status
    :param item_status: New Item Status
    :param item_index: Index of Item to be changed
    :return: New Bank Status
    """
    item_index -= 1
    if item_index > 27:
        # TODO: log warning
        return bank_status

    mask = ~(0b11 << (2 * item_index))

    return (bank_status & mask) | item_status << (2 * item_index)


T = TypeVar("T")


def with_fallback(v: T | None, fallback: T) -> T:
    if v is None:
        return fallback
    return v
