# meta2itol
tabular metadata files converted to colour strip inputs for iTOL

##Usage
    usage: meta_2_itol_strip.py [-h] -m METADATA -o OUTPUTPREFIX [-c COLUMNS] [-t TIP_ID] [-s SEP]
    
    optional arguments:
      -h, --help            show this help message and exit
      -m METADATA, --metadata METADATA
                            input metadata file (default: None)
      -o OUTPUTPREFIX, --outputprefix OUTPUTPREFIX
                            output prefix, each colum name will be appended to this to generate ouput files (default: None)
      -c COLUMNS, --columns COLUMNS
                            list (comma separated) of columns to generate colour strips for (default: all)
      -t TIP_ID, --tip_id TIP_ID
                            column header with strain ids matching tree tips (default: Strain)
      -s SEP, --sep SEP     delimiter between columns (default: )

###Input

Delimited file with one column matching the leaves of the tree you wish to annotate in iTOL

###Output

One colourstrip file for each metadata column, named by the column header