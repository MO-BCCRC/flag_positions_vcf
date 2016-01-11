#flag_positions_vcf : flag positions matching positions in a database (for vcf files)


```
Development information

date created : Jul 31 2014
last update  : 6 May 2015 by jrosner
Developer    : csiu
Input        : vcf file,
               vcf file containing a list of positions to mark as T,
               string
Output       : Flagged vcf file
Seed used    : flagPos.py

```


###Usage
To flag the info column of a vcf file -- using the positions from another _"database"_ vcf file -- with something like `string=T` or `string=F` or user can specify a column containing an id to be used for the flag value
The database file must be tab separated where the first two columns are:
1/ chromosome
2/ position


###Dependencies

- python version >= 2.7

