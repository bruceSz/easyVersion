
import unittest
from ev import sub_commands

class test_sub_commands(unittest.TestCase):

    def setUp(self):
        sub_commands.setup_router()
        self.router = sub_commands.ROUTER 

    def test_sub_commands(self):
        # this test case just guarantee below commands are added into the
        # router . Actual execute of those functions is not tested.
        commands = ["track","untrack","history","checkout","comment"]
        for comm in commands:
            self.assertIn(comm in self.router )
            
            
        
