# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 20:57:59 2014

@author: emmanuel
"""

from DecToRoman import DecToRoman, DecToRomanUserError
import unittest

class testDecToRoman(unittest.TestCase):
    
    def setUp(self):
        self.decToRoman = DecToRoman()
    
    def test_one_digit_number(self):
        """verifica que la conversión de un numero de un dígito sea correcta"""
        roman = self.decToRoman.decimalToRoman("7")
        self.assertEqual(roman,"VII")
    
    def test_two_digits_number(self):
        """verifica que la conversión de un numero de dos dígitos sea correcta"""
        roman = self.decToRoman.decimalToRoman("68")
        self.assertEqual(roman,"LXVIII")       

    def test_three_digits_number(self):
        """verifica que la conversión de un numero de tres dígitos sea correcta"""
        roman = self.decToRoman.decimalToRoman("549")
        self.assertEqual(roman,"DXLIX")               

    def test_four_digits_number(self):
        """verifica que la conversión de un numero de 4 dígitos sea correcta"""
        roman = self.decToRoman.decimalToRoman("2134")
        self.assertEqual(roman,"MMCXXXIV")  
        
    def test_number_greater_than_Max_Number(self):
        """Prueba que arroje una excepción DecToRomanUserError si el número es mayor a decToRoman.maxNumber"""
        with self.assertRaisesRegexp(DecToRomanUserError, "the input must be a number lesser than " + repr(self.decToRoman.maxNumber)):
            romanOverMax = self.decToRoman.decimalToRoman(str(self.decToRoman.maxNumber + 1))
            

    def test_input_is_not_a_positive_integer(self):
        """Prueba que arroje una excepción DecToRomanUserError si el número es un negativo"""
        with self.assertRaisesRegexp(DecToRomanUserError, "Input must be a positive number"):
            romanSmalletZero = self.decToRoman.decimalToRoman("-1")
            
    def test_input_is_not_an_integer(self):
        """Prueba que arroje una excepción DecToRomanUserError si el número no es un entero"""
        with self.assertRaisesRegexp(DecToRomanUserError, "Input must be a positive number"):
            romanSmalletZero = self.decToRoman.decimalToRoman("3.1416")
            
    def test_input_contains_non_numeric_symbols(self):
        """Prueba que arroje una excepción DecToRomanUserError si el número contiene caracteres no numéricos como letras"""
        with self.assertRaisesRegexp(DecToRomanUserError, "Input must be a positive number"):
            romanSmalletZero = self.decToRoman.decimalToRoman("0es3") 
            
        
if __name__ == '__main__':
    unittest.main()
    
