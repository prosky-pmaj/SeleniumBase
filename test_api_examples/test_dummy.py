import math
import time
from unittest import TestCase

import apibase


class TestSimple(TestCase):
    def test_case1(self):
        #apibase.http.get("http://localhost:8003")
        with apibase.transaction("tran name"):
            for x in range(1000, 10000):
                y = math.sqrt(x)

    def test_case2(self):
        #apibase.http.get("http://apc-gw:8080")
        for x in range(1, 10):
            y = math.sqrt(x)
