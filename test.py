from utils import *
from constants import *
from config import *
import unittest

class Tests(unittest.TestCase):
    def test_get_sorted_families(self):
        self.assertEqual(get_sorted_families(vk,config['peer_id']), surnames)
    
    def test_command_from_text(self):
        self.assertEqual(command_from_text('бот, я все'),'я все')
        self.assertEqual(command_from_text('бот я все'),'я все')

if __name__ == '__main__':
    unittest.main()
    #get_sorted_families(vk,config['peer_id'])