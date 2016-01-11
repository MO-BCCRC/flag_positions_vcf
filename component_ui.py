# -*- coding: utf-8 -*-
'''
Created on 2014 July 31 (Thursday)

@author: csiu
'''

import argparse


#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(prog='flag positions',
         description='''To the end of the info column of a VCF,
         append "<string>=T" or "<string>=F" depending on whether
         position is found in the db (another VCF) file''')


parser.add_argument("--infile",
       required=True,
       help='''specify the path/to/VCF-formatted-input-file.vcf''')

parser.add_argument("--db",
       required=True,
       help='''specify the path/to/db.vcf file to be
       used as a reference to determine whether
       positions in input file is also in db''')

parser.add_argument("--out",
       required=True,
       help='''specify the path/to/out.vcf to save output to a file''')

parser.add_argument("--input_type",
                   required=True,
                   choices=['indel','snv'],
                   help='''snv or indel''')

parser.add_argument("--label",
               required=True,
               help='''specify a string/description
               to be used in "<string>=T" and "<string>=F"''')

parser.add_argument("--flag_with_id",
               action='store_true',
               help='''use an id for the flag''')

##get at the arguments
args, unknown = parser.parse_known_args()
