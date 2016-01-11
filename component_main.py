'''
adds a flag to the end of the info column of a vcf file

Created on 31 July 2014 (Thursday)

@author: csiu
'''

from kronos.utils import ComponentAbstract
import os

class Component(ComponentAbstract):
    '''Run flag.py, load dependencies and requirements'''

    def __init__(self, component_name='flag_positions_vcf', component_parent_dir=None, seed_dir=None):
        self.version = '1.1.0'

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk):

        cmd = self.requirements['python'] + ' ' + os.path.join(self.seed_dir, 'flagPos.py')
        cmd_args = ['--infile',     self.args.infile,
                    '--db',         self.args.db,
                    '--out',        self.args.out,
                    '--label',      self.args.label,
                    '--input_type', self.args.input_type,
                    '--tabix_path', self.args.tabix_path]

        if chunk is not None:
            cmd_args.extend(['--chrom', chunk])

        if self.args.flag_with_id:
            cmd_args.extend(['--flag_with_id', self.args.flag_with_id])

        return cmd, cmd_args


# to run as stand alone
def _main():
    fp = Component()
    fp.args = component_ui.args
    fp.run()

if __name__ == '__main__':
    import component_ui
    _main()
