import unittest
import unittest.mock

from testing.ClassToTest import ClassToTest


class TestClass(unittest.TestCase):
	def setUp(self) -> None:
		self.testClass = ClassToTest(3)

	def test_test_class(self):
		self.assertEquals(self.testClass.add(3), 6, "Wrong")
