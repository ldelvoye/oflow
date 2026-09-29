"""Helpers shared by the Spotify tests."""

from collections.abc import Callable
from io import BytesIO

import pytest
from PIL import Image


@pytest.fixture
def png() -> Callable[..., bytes]:
    """Builds the PNG bytes of one solid-colour square."""

    def make(color: tuple[int, int, int] = (255, 0, 0), size: int = 8) -> bytes:
        image = Image.new("RGB", (size, size), color)
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        return buffer.getvalue()

    return make
