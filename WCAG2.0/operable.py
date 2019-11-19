#https://www.w3.org/TR/WCAG20/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

#Operable

#2.1.1 Keyboard
"""
!! I need to verify that keyboard focus can be used with selenium, and if so, that it 
follows the same machinations that the standard use of keyboard navigations uses.

a. Verify that if given x element, then that element will be focusable if all elements 
on page are focused one after another.
"""

#2.1.2 No Keyboard Trap
"""
!! Refer to note in 2.1.1
For all elements:
a. Starting with x element, check to see if the x+1 is selectable.
b. Starting with x element, check to see if the x-1 element is selectable.
c. Starting with x element, check to see if the x+1 element is selectable.
d. Proceed to last element.
e. Proceed to first element.
"""

#2.1.3 Keyboard (No exception)
"""
"""

#2.2.1 Timing Adjustable
"""
"""

#2.2.2 Pause, Stop, Hide
"""
"""

#2.2.3 No Timing
"""
!! Event listener.
a. Idle page for x amount of time. Verify page has not changed after x amount of time.
"""

#2.2.4 Interruptions
"""
"""

#2.2.5 Re-authenticating
"""
"""

#2.3.1 Three Flashes or Below Threshold
"""
!! Event listener
a. On event, add to count. After 1 second, verify count < 3.

b. verify color of content flashing isn't red. 
!! Might not be possible if it's an imported object.
"""

#2.3.2 Three Flashes
"""
"""

#2.4.1 Bypass Blocks
"""
"""

# 2.4.2 Page Titled
"""
Verify that the title is differant from the previous page.
Check For generic title. 
    - save main page title to compare against
"""

#2.4.3 Focus Order
"""
"""

#2.4.4 Link Purpose
"""
Look for aria-label attribute for link purpose 
Look for alt attribute for link purpose
"""

#2.4.5 Multiple Ways
"""
"""

#2.4.6 Headings and Labels
"""
"""

#2.4.7 Focus Visible
"""
"""

#2.4.8 Location
"""
"""

#2.4.9 Link Purpose (Link Only)
"""
"""

#2.4.10 Section Headings
"""
"""