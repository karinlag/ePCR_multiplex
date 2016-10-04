# ePRC multiplex

This directory contains the python version 2 script **ePCR_multiplex.py** which can be used to 
create a multiplexed input file for the [ePCR](http://www.ncbi.nlm.nih.gov/tools/epcr/) program.

## How it works

Input: 

 * name of fasta formatted file containing primers.  Note: any lines in this input file 
that start with a "#" are skipped to allow for comments in the file.
 * name of output file
 * whether to allow primer self pairs or not (default is no) 

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

provided that self pairs are not allowed. If self pairs are allowed, there
will be three extra lines of output, one for each self pair.

The output file is tab separated, and has three columns.

## How to run

Options are:  
    -p, --primer        name of file containing primers  
    -o, --outfile       name of output file  
    -s, --selfprimer    specify for primer self pairing

From the command line:

Without self priming (i.e. default):

    python ePCR_multiplex.py -p <name of file containing primers> -o <name of output file>

With self priming:

    python ePCR_multiplex.py -p <name of file containing primers> -o <name of output file> -s