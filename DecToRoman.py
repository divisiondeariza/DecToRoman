# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:15:21 2014

@author: Emmanuel Ariza
"""

import re

"""
Esta es la clase de un convertidor de números decimales a dígitos.
"""
class DecToRoman:
    """número mayor que se puede convertir a número Romano"""
    maxNumber = 3000 
    
    def __init__(self):
        """
        Lista de todos los simbolos romanos clasificados por su significado en unidades, decenas,
        dentenas y millares.
        Al dicionario de millares se agregan los símbolos V* y X* a pesar de que no serán usados para que
        sea consistente con los otros diccionarios
        """        
        self._symbols = [{1:'I', 5:'V', 10:'X', "digitType":"units"}, 
                         {1:'X', 5:'L', 10:'C', "digitType":"tents"}, 
                         {1:'C', 5:'D', 10:'M', "digitType":"cents"}, 
                         {1:'M', 5:'V*', 10:'X*', "digitType":"thousands"}]  

    """
    Convierte un solo dígito en un número romano.
    Aprovechando que las reglas de los números romanos son iguales para los dígitos correspondientes
    unidades, decenas y centenas, se usa esta función para varios tipos de dígitos, dando como parámetro
    adicional las "letras" a las que correspondientemente se transformará según si es unidad, decena, 
    centena o millar.
    
    Parámetros:
     - Digit: dígito a ser convertido
     - letters: conjunto de letras al que será re-mapeado.
    """
    
    def _digitToRoman(self, digit, letters):

        if digit <= 3:
            return letters[1]*digit
        elif digit == 4:
            return letters[1] + letters[5]
        elif digit <= 8:
            return letters[5] + letters[1]*(digit-5)
        elif digit == 9:
            return letters[1] + letters[10]
        else:
            raise ValueError(digit + " is not a digit, it should be between 0 and 9")
        
            
    """
    función que convierte el decimal en número romano concatenando los resultados de la conversión de
    unidades, decenas, centenas, etc de la función self._digitToRoman()
    
    Parámetros:
     - dec: número decimal a convertir, es una cadena de caracteres numéricos.
    """
    
    def decimalToRoman(self, strDec):
        dec = self._userInputToInt(strDec)
        
        if self.maxNumber < dec:
            raise DecToRomanUserError("the input must be a number lesser than " + repr(self.maxNumber))
 
        roman = ""
        for letters in self._symbols:
            digit = dec%10 #módulo
            #print letters["digitType"] + " " + str(digit)            
            roman = self._digitToRoman(digit, letters) + roman
            dec= dec/10 #División Entera
            
        return roman
    
    """
    Convierte el valor de entrada (una cadena) en un entero, si la cadena no es válida arroja una excepción DecToRomanUserError
    Parámetro:
     - strInput: Cadena de entrada
    """
    def _userInputToInt(self,strInput):
        if not re.match(r"^\d*$",strInput) :
            raise DecToRomanUserError("Input must be a positive number")
        else:
            return int(strInput)
        
"""
    Esta excepción se arroja cuando una operación en DecToRoman causados por entradas del usuario no válidas.

"""

class DecToRomanUserError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)


if __name__ == "__main__":
    """crea el convertidor"""
    decToRoman = DecToRoman()
    
    """ variables de cadenas para colorear la consola"""
    bluePrompt = chr(27) + "[0;36m"
    redPrompt = chr(27) + "[0;31m" 
    endColorPromt = chr(27) + "[0m"
    
    
    print bluePrompt + ":::: Arabic - Roman number converter ::::" + endColorPromt
    
    """
    Solicila el número de entrada al usuario, en caso de que este ingrese un valor inválido preguntará de nuevo
    """
    while True:
        strDec = raw_input("please enter an arabic number between 0 and " + str(decToRoman.maxNumber) + " you want to convert to decimal:\n")
    
        try:
            print "The number " + strDec + " is in roman " + bluePrompt + decToRoman.decimalToRoman(strDec) + endColorPromt
            break
    
        except DecToRomanUserError as e:
            print redPrompt + "Error:" + e.msg + ", please try again" + endColorPromt
        
    
