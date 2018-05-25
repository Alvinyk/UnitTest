import unittest
from TestRunner import MyTestRunner
from name_function import *

class NamesTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_middle_last_name(self):
        full_name = get_full_name('first','middle','last')
        self.assertEqual(full_name, 'First Middle Last')
        
        
if __name__ == '__main__':
    unittest.main(testRunner=MyTestRunner)
    