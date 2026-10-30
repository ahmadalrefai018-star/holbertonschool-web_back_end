#!/usr/bin/env python3
"""Generate ten random numbers asynchronously."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield a random float after each one-second asynchronous wait."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
