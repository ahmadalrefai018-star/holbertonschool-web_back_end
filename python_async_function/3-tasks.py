#!/usr/bin/env python3
"""Create an asyncio task for a random-delay coroutine."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Schedule wait_random as a task and return the task."""
    return asyncio.create_task(wait_random(max_delay))
