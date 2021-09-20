import unittest
from diagnose import Diseases

class TestDiseases(unittest.TestCase):

	def test_d1(self):
		d1 = Diseases("Ferrugem Comum", 16, 23, 95, 100, 0, 1023)
		self.assertEqual (d1.checkIfPossible(10, 90, 0), 1)
		self.assertEqual (d1.checkIfPossible(16, 90, 0), 2)
		self.assertEqual (d1.checkIfPossible(20, 90, 0), 2)
		self.assertEqual (d1.checkIfPossible(23, 90, 0), 2)
		self.assertEqual (d1.checkIfPossible(30, 90, 0), 1)

		# variando umi para cada temp. luz 0
		self.assertEqual (d1.checkIfPossible(10, 95, 0), 2)
		self.assertEqual (d1.checkIfPossible(10, 97, 0), 2)
		self.assertEqual (d1.checkIfPossible(10, 100, 0), 2)

		self.assertEqual (d1.checkIfPossible(16, 95, 0), 3)
		self.assertEqual (d1.checkIfPossible(16, 97, 0), 3)
		self.assertEqual (d1.checkIfPossible(16, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(20, 95, 0), 3)
		self.assertEqual (d1.checkIfPossible(20, 97, 0), 3)
		self.assertEqual (d1.checkIfPossible(20, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(23, 95, 0), 3)
		self.assertEqual (d1.checkIfPossible(23, 97, 0), 3)
		self.assertEqual (d1.checkIfPossible(23, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(30, 95, 0), 2)
		self.assertEqual (d1.checkIfPossible(30, 97, 0), 2)
		self.assertEqual (d1.checkIfPossible(30, 100, 0), 2)

		# variando luz para cada umi e temp. luz 500

		self.assertEqual (d1.checkIfPossible(10, 95, 500), 2)
		self.assertEqual (d1.checkIfPossible(10, 97, 500), 2)
		self.assertEqual (d1.checkIfPossible(10, 100, 500), 2)

		self.assertEqual (d1.checkIfPossible(16, 95, 500), 3)
		self.assertEqual (d1.checkIfPossible(16, 97, 500), 3)
		self.assertEqual (d1.checkIfPossible(16, 100, 500), 3)

		self.assertEqual (d1.checkIfPossible(20, 95, 500), 3)
		self.assertEqual (d1.checkIfPossible(20, 97, 500), 3)
		self.assertEqual (d1.checkIfPossible(20, 100, 500), 3)

		self.assertEqual (d1.checkIfPossible(23, 95, 500), 3)
		self.assertEqual (d1.checkIfPossible(23, 97, 500), 3)
		self.assertEqual (d1.checkIfPossible(23, 100, 500), 3)

		self.assertEqual (d1.checkIfPossible(30, 95, 500), 2)
		self.assertEqual (d1.checkIfPossible(30, 97, 500), 2)
		self.assertEqual (d1.checkIfPossible(30, 100, 500), 2)

		# variando luz para cada umi e temp. luz 1023
		self.assertEqual (d1.checkIfPossible(10, 95, 1023), 2)
		self.assertEqual (d1.checkIfPossible(10, 97, 1023), 2)
		self.assertEqual (d1.checkIfPossible(10, 100, 1023), 2)

		self.assertEqual (d1.checkIfPossible(16, 95, 1023), 3)
		self.assertEqual (d1.checkIfPossible(16, 97, 1023), 3)
		self.assertEqual (d1.checkIfPossible(16, 100, 1023), 3)

		self.assertEqual (d1.checkIfPossible(20, 95, 1023), 3)
		self.assertEqual (d1.checkIfPossible(20, 97, 1023), 3)
		self.assertEqual (d1.checkIfPossible(20, 100, 1023), 3)

		self.assertEqual (d1.checkIfPossible(23, 95, 1023), 3)
		self.assertEqual (d1.checkIfPossible(23, 97, 1023), 3)
		self.assertEqual (d1.checkIfPossible(23, 100, 1023), 3)

		self.assertEqual (d1.checkIfPossible(30, 95, 1023), 2)
		self.assertEqual (d1.checkIfPossible(30, 97, 1023), 2)
		self.assertEqual (d1.checkIfPossible(30, 100, 1023), 2)

	def test_d2(self):
		d1 = Diseases("Mancha de Phaeosphaeria", 0, 14, 60, 100, 0, 150)
		self.assertEqual (d1.checkIfPossible(-10, 50, 0), 1)
		self.assertEqual (d1.checkIfPossible(0, 50, 0), 2)
		self.assertEqual (d1.checkIfPossible(7, 50, 0), 2)
		self.assertEqual (d1.checkIfPossible(14, 50, 0), 2)
		self.assertEqual (d1.checkIfPossible(20, 50, 0), 1)

		# variando umi para cada temp. luz 0
		self.assertEqual (d1.checkIfPossible(-10, 60, 0), 2)
		self.assertEqual (d1.checkIfPossible(-10, 70, 0), 2)
		self.assertEqual (d1.checkIfPossible(-10, 100, 0), 2)

		self.assertEqual (d1.checkIfPossible(0, 60, 0), 3)
		self.assertEqual (d1.checkIfPossible(0, 70, 0), 3)
		self.assertEqual (d1.checkIfPossible(0, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(7, 60, 0), 3)
		self.assertEqual (d1.checkIfPossible(7, 70, 0), 3)
		self.assertEqual (d1.checkIfPossible(7, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(14, 60, 0), 3)
		self.assertEqual (d1.checkIfPossible(14, 70, 0), 3)
		self.assertEqual (d1.checkIfPossible(14, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(20, 60, 0), 2)
		self.assertEqual (d1.checkIfPossible(20, 70, 0), 2)
		self.assertEqual (d1.checkIfPossible(20, 100, 0), 2)

		# variando luz para cada umi e temp. luz 500

		self.assertEqual (d1.checkIfPossible(-10, 60, 70), 2)
		self.assertEqual (d1.checkIfPossible(-10, 70, 70), 2)
		self.assertEqual (d1.checkIfPossible(-10, 100, 70), 2)

		self.assertEqual (d1.checkIfPossible(0, 60, 70), 3)
		self.assertEqual (d1.checkIfPossible(0, 70, 70), 3)
		self.assertEqual (d1.checkIfPossible(0, 100, 70), 3)

		self.assertEqual (d1.checkIfPossible(7, 60, 70), 3)
		self.assertEqual (d1.checkIfPossible(7, 70, 70), 3)
		self.assertEqual (d1.checkIfPossible(7, 100, 70), 3)

		self.assertEqual (d1.checkIfPossible(14, 60, 70), 3)
		self.assertEqual (d1.checkIfPossible(14, 70, 70), 3)
		self.assertEqual (d1.checkIfPossible(14, 100, 70), 3)

		self.assertEqual (d1.checkIfPossible(20, 60, 70), 2)
		self.assertEqual (d1.checkIfPossible(20, 70, 70), 2)
		self.assertEqual (d1.checkIfPossible(20, 100, 70), 2)

		# variando luz para cada umi e temp. luz 1023
		self.assertEqual (d1.checkIfPossible(-10, 60, 150), 2)
		self.assertEqual (d1.checkIfPossible(-10, 70, 150), 2)
		self.assertEqual (d1.checkIfPossible(-10, 100, 150), 2)

		self.assertEqual (d1.checkIfPossible(0, 60, 150), 3)
		self.assertEqual (d1.checkIfPossible(0, 70, 150), 3)
		self.assertEqual (d1.checkIfPossible(0, 100, 150), 3)

		self.assertEqual (d1.checkIfPossible(7, 60, 150), 3)
		self.assertEqual (d1.checkIfPossible(7, 70, 150), 3)
		self.assertEqual (d1.checkIfPossible(7, 100, 150), 3)

		self.assertEqual (d1.checkIfPossible(14, 60, 150), 3)
		self.assertEqual (d1.checkIfPossible(14, 70, 150), 3)
		self.assertEqual (d1.checkIfPossible(14, 100, 150), 3)

		self.assertEqual (d1.checkIfPossible(20, 60, 150), 2)
		self.assertEqual (d1.checkIfPossible(20, 70, 150), 2)
		self.assertEqual (d1.checkIfPossible(20, 100, 150), 2)

		# variando luz para cada umi e temp. luz 1023
		self.assertEqual (d1.checkIfPossible(-10, 60, 1023), 1)
		self.assertEqual (d1.checkIfPossible(-10, 70, 1023), 1)
		self.assertEqual (d1.checkIfPossible(-10, 100, 1023), 1)

		self.assertEqual (d1.checkIfPossible(0, 60, 1023), 2)
		self.assertEqual (d1.checkIfPossible(0, 70, 1023), 2)
		self.assertEqual (d1.checkIfPossible(0, 100, 1023), 2)

		self.assertEqual (d1.checkIfPossible(7, 60, 1023), 2)
		self.assertEqual (d1.checkIfPossible(7, 70, 1023), 2)
		self.assertEqual (d1.checkIfPossible(7, 100, 1023), 2)

		self.assertEqual (d1.checkIfPossible(14, 60, 1023), 2)
		self.assertEqual (d1.checkIfPossible(14, 70, 1023), 2)
		self.assertEqual (d1.checkIfPossible(14, 100, 1023), 2)

		self.assertEqual (d1.checkIfPossible(20, 60, 1023), 1)
		self.assertEqual (d1.checkIfPossible(20, 70, 1023), 1)
		self.assertEqual (d1.checkIfPossible(20, 100, 1023), 1)

	def test_d3(self):
		d1 = Diseases("Ferrugem Comum", 16, 23, 95, 100, 0, 1023)
		self.assertEqual (d1.checkIfPossible(10, 90, 0), 1)
		self.assertEqual (d1.checkIfPossible(16, 90, 0), 2)
		self.assertEqual (d1.checkIfPossible(20, 90, 0), 2)
		self.assertEqual (d1.checkIfPossible(23, 90, 0), 2)
		self.assertEqual (d1.checkIfPossible(30, 90, 0), 1)

		# variando umi para cada temp. luz 0
		self.assertEqual (d1.checkIfPossible(10, 95, 0), 2)
		self.assertEqual (d1.checkIfPossible(10, 97, 0), 2)
		self.assertEqual (d1.checkIfPossible(10, 100, 0), 2)

		self.assertEqual (d1.checkIfPossible(16, 95, 0), 3)
		self.assertEqual (d1.checkIfPossible(16, 97, 0), 3)
		self.assertEqual (d1.checkIfPossible(16, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(20, 95, 0), 3)
		self.assertEqual (d1.checkIfPossible(20, 97, 0), 3)
		self.assertEqual (d1.checkIfPossible(20, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(23, 95, 0), 3)
		self.assertEqual (d1.checkIfPossible(23, 97, 0), 3)
		self.assertEqual (d1.checkIfPossible(23, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(30, 95, 0), 2)
		self.assertEqual (d1.checkIfPossible(30, 97, 0), 2)
		self.assertEqual (d1.checkIfPossible(30, 100, 0), 2)

		# variando luz para cada umi e temp. luz 500

		self.assertEqual (d1.checkIfPossible(10, 95, 500), 2)
		self.assertEqual (d1.checkIfPossible(10, 97, 500), 2)
		self.assertEqual (d1.checkIfPossible(10, 100, 500), 2)

		self.assertEqual (d1.checkIfPossible(16, 95, 500), 3)
		self.assertEqual (d1.checkIfPossible(16, 97, 500), 3)
		self.assertEqual (d1.checkIfPossible(16, 100, 500), 3)

		self.assertEqual (d1.checkIfPossible(20, 95, 500), 3)
		self.assertEqual (d1.checkIfPossible(20, 97, 500), 3)
		self.assertEqual (d1.checkIfPossible(20, 100, 500), 3)

		self.assertEqual (d1.checkIfPossible(23, 95, 500), 3)
		self.assertEqual (d1.checkIfPossible(23, 97, 500), 3)
		self.assertEqual (d1.checkIfPossible(23, 100, 500), 3)

		self.assertEqual (d1.checkIfPossible(30, 95, 500), 2)
		self.assertEqual (d1.checkIfPossible(30, 97, 500), 2)
		self.assertEqual (d1.checkIfPossible(30, 100, 500), 2)

		# variando luz para cada umi e temp. luz 1023
		self.assertEqual (d1.checkIfPossible(10, 95, 1023), 2)
		self.assertEqual (d1.checkIfPossible(10, 97, 1023), 2)
		self.assertEqual (d1.checkIfPossible(10, 100, 1023), 2)

		self.assertEqual (d1.checkIfPossible(16, 95, 1023), 3)
		self.assertEqual (d1.checkIfPossible(16, 97, 1023), 3)
		self.assertEqual (d1.checkIfPossible(16, 100, 1023), 3)

		self.assertEqual (d1.checkIfPossible(20, 95, 1023), 3)
		self.assertEqual (d1.checkIfPossible(20, 97, 1023), 3)
		self.assertEqual (d1.checkIfPossible(20, 100, 1023), 3)

		self.assertEqual (d1.checkIfPossible(23, 95, 1023), 3)
		self.assertEqual (d1.checkIfPossible(23, 97, 1023), 3)
		self.assertEqual (d1.checkIfPossible(23, 100, 1023), 3)

		self.assertEqual (d1.checkIfPossible(30, 95, 1023), 2)
		self.assertEqual (d1.checkIfPossible(30, 97, 1023), 2)
		self.assertEqual (d1.checkIfPossible(30, 100, 1023), 2)

	def test_d4(self):
		d1 = Diseases("Podridao de Stenocarpella", 28, 30, 95, 100, 0, 1023)
		self.assertEqual (d1.checkIfPossible(10, 90, 0), 1)
		self.assertEqual (d1.checkIfPossible(28, 90, 0), 2)
		self.assertEqual (d1.checkIfPossible(29, 90, 0), 2)
		self.assertEqual (d1.checkIfPossible(30, 90, 0), 2)
		self.assertEqual (d1.checkIfPossible(40, 90, 0), 1)

		# variando umi para cada temp. luz 0
		self.assertEqual (d1.checkIfPossible(10, 95, 0), 2)
		self.assertEqual (d1.checkIfPossible(10, 97, 0), 2)
		self.assertEqual (d1.checkIfPossible(10, 100, 0), 2)

		self.assertEqual (d1.checkIfPossible(28, 95, 0), 3)
		self.assertEqual (d1.checkIfPossible(28, 97, 0), 3)
		self.assertEqual (d1.checkIfPossible(28, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(29, 95, 0), 3)
		self.assertEqual (d1.checkIfPossible(29, 97, 0), 3)
		self.assertEqual (d1.checkIfPossible(29, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(30, 95, 0), 3)
		self.assertEqual (d1.checkIfPossible(30, 97, 0), 3)
		self.assertEqual (d1.checkIfPossible(30, 100, 0), 3)

		self.assertEqual (d1.checkIfPossible(40, 95, 0), 2)
		self.assertEqual (d1.checkIfPossible(40, 97, 0), 2)
		self.assertEqual (d1.checkIfPossible(40, 100, 0), 2)

		# variando luz para cada umi e temp. luz 500

		self.assertEqual (d1.checkIfPossible(10, 95, 500), 2)
		self.assertEqual (d1.checkIfPossible(10, 97, 500), 2)
		self.assertEqual (d1.checkIfPossible(10, 100, 500), 2)

		self.assertEqual (d1.checkIfPossible(28, 95, 500), 3)
		self.assertEqual (d1.checkIfPossible(28, 97, 500), 3)
		self.assertEqual (d1.checkIfPossible(28, 100, 500), 3)

		self.assertEqual (d1.checkIfPossible(29, 95, 500), 3)
		self.assertEqual (d1.checkIfPossible(29, 97, 500), 3)
		self.assertEqual (d1.checkIfPossible(29, 100, 500), 3)

		self.assertEqual (d1.checkIfPossible(30, 95, 500), 3)
		self.assertEqual (d1.checkIfPossible(30, 97, 500), 3)
		self.assertEqual (d1.checkIfPossible(30, 100, 500), 3)

		self.assertEqual (d1.checkIfPossible(40, 95, 500), 2)
		self.assertEqual (d1.checkIfPossible(40, 97, 500), 2)
		self.assertEqual (d1.checkIfPossible(40, 100, 500), 2)

		# variando luz para cada umi e temp. luz 1023
		self.assertEqual (d1.checkIfPossible(10, 95, 1023), 2)
		self.assertEqual (d1.checkIfPossible(10, 97, 1023), 2)
		self.assertEqual (d1.checkIfPossible(10, 100, 1023), 2)

		self.assertEqual (d1.checkIfPossible(28, 95, 1023), 3)
		self.assertEqual (d1.checkIfPossible(28, 97, 1023), 3)
		self.assertEqual (d1.checkIfPossible(28, 100, 1023), 3)

		self.assertEqual (d1.checkIfPossible(29, 95, 1023), 3)
		self.assertEqual (d1.checkIfPossible(29, 97, 1023), 3)
		self.assertEqual (d1.checkIfPossible(29, 100, 1023), 3)

		self.assertEqual (d1.checkIfPossible(30, 95, 1023), 3)
		self.assertEqual (d1.checkIfPossible(30, 97, 1023), 3)
		self.assertEqual (d1.checkIfPossible(30, 100, 1023), 3)

		self.assertEqual (d1.checkIfPossible(40, 95, 1023), 2)
		self.assertEqual (d1.checkIfPossible(40, 97, 1023), 2)
		self.assertEqual (d1.checkIfPossible(40, 100, 1023), 2)
