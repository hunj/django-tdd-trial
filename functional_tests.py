from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def teardown(self):
        self.browser.quit()
        
    def test_can_visit_frontpage(self):
        # visit the front page
        self.browser.get('http://localhost:8000')
        # the page title should say "Resources"
        self.assertIn('Resources', self.browser.title)
        self.fail('force quitting test!')
    

if __name__ == '__main__':
    unittest.main(warnings='ignore')