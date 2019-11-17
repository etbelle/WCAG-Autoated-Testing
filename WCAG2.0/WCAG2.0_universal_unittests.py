#https://www.w3.org/TR/WCAG20/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


#Perceivable

# 1.1.1 Non-text Content
"""
a. Compare x against y text
	- If x in y
	
b. confirm <* alt="*"> == True, i.e. there is Alt attribute available.
"""

#1.2.1 Audio-only and Video-only (Prerecorded)
"""
!! each video player is a bit different.
"""

#1.2.2 Captions (Prerecorded)
"""
!! See note on 1.2.1
"""

#1.2.3 Audio Description or Media Alternative (Prerecorded)
"""
!! Audio descriptions can be provided either as body text or download
	- both of which should be tied to each other via name, but that isn't officially part of the guideline.
"""

#1.2.4 Captions (Live)
"""
!! See note on 1.2.1
"""

#1.2.5 Audio Description (Prerecorded)
"""
!! See 1.2.3
"""

#1.2.6 Sign Language (Prerecorded)
"""

"""

#1.2.7 Extended Audio Description (Prerecorded)
"""
"""

#1.2.8 Media Alternative (Prerecorded)
"""
"""

#1.2.9 Audio-only (Live)
"""
"""

#1.3.1 Info and Relationships
"""
"""

#1.3.2 Meaningful Sequence
"""

"""

#1.3.3 Sensory Characteristics
"""
"""

#1.4.1 Use of Color
"""
a. Check for difference between body text style and link style:
	- font
	- Size
	- bold/italics/underline
	- color
"""

#1.4.2 Audio Control
"""
"""

#1.4.3 Contrast (Minimum)
"""
a. Check that the text is a decorative or inactive.

b. If text is large, check if contrast ratio is of as least 3:1

c. Check that the text has a contrast ratio of 4.5:1
"""

#1.4.4 Resize text
"""
!! I think selenium can manipulate a website on the fly. More research needed.
"""

#1.4.5 Images of Text
"""
a. Check if heading has a img attribute and no actual text. 

!! It might be possible that there are common phrases to look for in the img file names or alt text, but nothing would be in absolute terms.
"""

#1.4.6 Contrast (Enhanced)
"""
!! See 1.4.3
"""

#1.4.7 Low or No Background Audio
"""

"""

#1.4.8 Visual Presentation
"""
"""

#1.4.9 Images of Text (No Exception)
"""
"""


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


#Understandable

#3.1.1 Language of Page
"""
"""

#3.1.2 Language of Parts
"""
"""

#3.1.3 Unusual Words
"""
"""

#3.1.4 Abbreviations
"""
"""

#3.1.5 Reading Level
"""
"""

#3.1.6 Pronunciation
"""
"""

#3.2.1 On Focus
"""
"""

#3.2.2 On Input
"""
"""

#3.2.3 Consistent Navigation
"""
"""

#3.2.4 Consistent Identification
"""
"""

#3.2.5 Change on Request
"""
"""

#3.3.1 Error Identification
"""
"""

#3.3.2 Labels or Instructions
"""
"""

#3.3.3 Error Suggestion
"""
"""

#3.3.4 Error Prevention (Legal, Financial, Data)
"""
"""

#3.3.5 Help
"""
"""

#3.3.6 Error prevention (All)
"""
"""


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