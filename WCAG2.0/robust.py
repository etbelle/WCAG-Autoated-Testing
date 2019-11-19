#https://www.w3.org/TR/WCAG20/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

#Robust 

#4.1.1 Parsing
"""
USE W3C VALIDATOR: https://pypi.org/project/Online-W3C-Validator/ 
"""

#4.1.2 Name, Role, Value
"""
HTML tags have appropriate Name, Role, Value, and if appropriate, "checked" 
    - State https://www.w3.org/TR/2016/NOTE-WCAG20-TECHS-20161007/H91
If standard HTML element used, ensure there is a ARIA label.
Ensure aria-labelledby is used 
"""

