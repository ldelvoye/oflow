"""Tests for converting album artwork bytes into colored ASCII."""

from rich.style import Style
from rich.text import Text

from smorg.integrations.spotify.albumart import image_to_ascii


def test_a_square_image_is_half_as_tall_as_it_is_wide(png):
    rendered = image_to_ascii(png(), width=20)

    assert rendered is not None
    lines = rendered.plain.splitlines()
    assert len(lines) == 10
    assert all(len(line) == 20 for line in lines)


def test_pixels_carry_their_color(png):
    rendered = image_to_ascii(png((0, 128, 255)), width=4)

    assert rendered is not None
    assert isinstance(rendered, Text)
    spans = rendered._spans
    assert spans
    first_style = spans[0].style
    assert isinstance(first_style, Style)
    color = first_style.color
    assert color is not None
    triplet = color.triplet
    assert triplet is not None
    assert triplet.blue > triplet.red


def test_unreadable_bytes_yield_nothing(png):
    assert image_to_ascii(b"not an image", width=12) is None
    assert image_to_ascii(b"", width=12) is None
    assert image_to_ascii(png(), width=0) is None
