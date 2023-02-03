import unittest
import game


class TestGame(unittest.TestCase):
    # test if guess == answer
    def test_input(self):
        answer = 5
        guess = 5
        result = game.run(answer, guess)
        self.assertTrue(result)

    # test wrong guess
    def test_input_wrong_guess(self):
        result = game.run(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = game.run(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = game.run('5', 11)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
