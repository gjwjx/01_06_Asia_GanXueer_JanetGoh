import unittest
import pythonProject as project

class testProject(unittest.TestCase):

    def test_sum(self):
        result = project.Testing.add(42860566, 27353174, 26781571)
        self.assertEqual(result, 565748494)

    def test_mean(self):
        num = project.top3Countries
        result = round(project.Testing.mean(num), 1)
        self.assertEqual(result, 32331770.3)

