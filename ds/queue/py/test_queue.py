from queue import Queue

import pytest


def test_enqueue():
    queue = Queue()
    assert queue.is_empty()
