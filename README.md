# ePRC multiplex

This directory contains the python version 2 script **ePCR_multiplex.py** which can be used to 
create a multiplexed input file for the [ePCR](http://www.ncbi.nlm.nih.gov/tools/epcr/) program.

## How it works

Input: 

 * name of fasta formatted file containing primers.  Note: any lines in this input file 
that start with a "#" are skipped to allow for comments in the file.
 * name of output file
 

Output:

If the following three primers are included:

    >primer1_name
    AAAA
    >primer2_name
    TTTT
    >primer3_name
    CCCC
    
the output will look like this:

    primer1_name&primer2_name   AAAA    TTTT  
    primer1_name&primer3_name   AAAA    CCCC  
    primer2_name&primer3_name   TTTT    CCCC  

with tabs separating the three columns.

## How to run

Options are:  
    -p, --primer   name of file containing primers  
    -o, --outfile  name of output file  

From the command line:

    python ePCR_multiplex.py -p <name of file containing primers> -o <name of output file>

