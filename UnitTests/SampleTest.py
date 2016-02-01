import unittest


# class SimplisticTest(unittest.TestCase):
#
#     def test(self):
#         self.assertTrue(False)


class OutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True, msg='Fuck yeah!')

    def test_fail(self):
        self.assertFalse(False, msg='Test failed here')

    def test_error(self):
        raise RuntimeError('Test error!')

if __name__ == '__main__':
    unittest.main()
