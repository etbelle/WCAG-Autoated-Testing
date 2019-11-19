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

class non_text_content(unittest.TestCase):
    def test_a(self):
        

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
