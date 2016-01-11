'''
Created on Jun 17, 2014

@author: dgrewal
##tests for the count_component
'''

import unittest
import component_reqs, component_main
import subprocess
import os
from collections import defaultdict

class args():
    def __init__(self):
        self.infile  = '/sample/path/checks/make_cmd/infile'
        self.db      = '/sample/path/checks/make_cmd/db'
        self.out = '/sample/path/checks/make_cmd/outfile'
        self.string  = 'somestring'
        
class check_requirements(unittest.TestCase):
    def setUp(self):
        self.args = args()
        
    def test_make_cmd(self):
        comp = component_main.Component()
        comp.args = self.args
        cmd,cmd_args = comp.make_cmd(None)
        cmd_args = ' '.join(map(str,cmd_args))
        
        #The actual resulting command:
        real_command = component_reqs.requirements['python'] + ' ' + os.path.abspath('./component_seed')+'/flagPos.py'
        
        real_command_args = ['--infile '+self.args.infile,
                             '--db '+self.args.db,
                             '--out '+self.args.out,
                             '--string '+self.args.string
                             ]
        
        real_command_args = ' '.join(real_command_args)
        
        #Ensure that the commands match exactly
        self.assertEqual(real_command, cmd, 'Please recheck the cmd variable in make_cmd')
        
        #Ensure that each of the args are present in the command args list
        #Exact match not possible since order can change 
        self.assertEqual(cmd_args, real_command_args, 'Please recheck the cmd_args variable in make_cmd')
                
    def test_params(self):
        try:
            from component_params import input_files,input_params,output_files,return_value
        except:
            self.assertEqual(True,False,'Please complete the params file')
        
        try:
            import component_ui   
        except:
            #cannot run this test if running in unittest mode as ui isn't available
            self.assertEqual(True, True, '') 
            return
            
        arg_act = defaultdict(tuple)
        for val in component_ui.parser._actions[1:]:
            arg_act[val.dest] = (val.required,val.default)
            if val.required == None:
                self.assertEqual(val.default, None, 'The optional argument: '+ val.dest+' has no default value')
        
        #merge all the dictionaries together
        params_dict = dict(input_files.items() + input_params.items() + output_files.items())
        
        for dest,(req,default) in arg_act.iteritems():
            if req == True:
                self.assertEqual(params_dict[dest], '__REQUIRED__', 'params and ui dont match')
            else:
                if not params_dict[dest] in [default,None]:
                    self.assertEqual(True, False, 'Please ensure that either default or ' +\
                                     '__OPTIONAL__ flag is provided for: '+params_dict[dest])
        
 
    
def run():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    
    checkreqs = loader.loadTestsFromTestCase(check_requirements)
    
    suite.addTests(checkreqs)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
