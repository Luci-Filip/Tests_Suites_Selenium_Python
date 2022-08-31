import unittest
import HtmlTestRunner

from test_alerts import Alerts
from test_complete_web_form import CompleteWebForm
from test_login import Login


class TestSuite(unittest.TestCase):

    def test_suite(self):  # numele metodei este predefinit si NU trebuie schimbat
        teste_de_rulat = unittest.TestSuite()
        # teste_de_rulat.addTests([]) metoda add tests, apelata fara parametru
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(CompleteWebForm),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts)
        ])

        runner = HtmlTestRunner.HTMLTestRunner\
        (
            combine_reports=True,
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

        runner.run(teste_de_rulat)
