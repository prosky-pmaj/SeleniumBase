from unittest import TestCase

import apibase


class TestTransactions(TestCase):
    def test_1_single_transaction(self):
        with apibase.transaction("single-transaction"):
            pass

    def test_2_two_transactions(self):
        with apibase.transaction("transaction-1"):
            pass
        with apibase.transaction("transaction-2"):
            pass

    def test_3_nested_transactions(self):
        with apibase.transaction("outer"):
            with apibase.transaction("inner"):
                pass

    def test_4_no_transactions(self):
        pass

    def test_5_apiritif_assertions(self):
        apibase.http.get("http://blazedemo.com/").assert_ok()

    def test_6_apiritif_assertions_failed(self):
        apibase.http.get("http://blazedemo.com/").assert_failed()  # this assertion intentionally fails
