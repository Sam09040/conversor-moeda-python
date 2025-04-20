
from time import sleep
import unittest
from unittest.mock import patch
from conversor import convertion, currency_choice, get_fluctuation, get_moeda, get_value

class TestConvertionFunction(unittest.TestCase):
    def test_brl_to_brl(self):
        moeda = 'BRL'
        self.assertEqual(convertion(moeda, moeda, 25), 25)
    
    def test_brl_to_usd(self):
        sleep(1)
        self.assertEqual(convertion('BRL', 'USD', 10), 1.714)

    def test_brl_to_eur(self):
        sleep(1)
        self.assertEqual(convertion('BRL', 'EUR', 2), 0.3014)
    
    def test_brl_to_krw(self):
        sleep(1)
        self.assertAlmostEqual(convertion('BRL', 'KRW', 50), 12119.85, 2)
        
    def test_get_moeda(self):
        self.assertEqual(get_moeda('4'), 'KRW')
        self.assertEqual(get_moeda('2'), 'USD')
                
    @patch('builtins.input', side_effect=['1', '8'])
    def test_currency_choice(self, mock_input):
        resultado1 = currency_choice()
        resultado2 = currency_choice()
        self.assertEqual(resultado1, '1')
        self.assertIsNone(resultado2)
        
    @patch('builtins.input', return_value='55,25')
    def test_get_value(self, mock_input):
        resultado = get_value()
        self.assertEqual(resultado, 55.25)
        
    @patch('builtins.input', side_effect=['1', '4'])
    def test_get_fluctuation(self, mock_input):
        ponto1 = get_fluctuation()
        ponto2 = get_fluctuation()
        self.assertEqual(ponto1, 2)
        self.assertEqual(ponto2, 4)
