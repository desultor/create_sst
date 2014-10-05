#!/usr/bin/env python

# would be more nicer to use pandas than csv, but I don't want any non-standard
# dependencies
import csv
import argparse

parser = argparse.ArgumentParser(description="Create a Raven Sound Selection \
        Table from batch detection tables. Print resulting table to standard \
        output or to a specified filename.")
# argument: sound file directory (all must be in same directory. this is possibly a requirement of batch detection itself?)
parser.add_argument("sound_file_directory",
        help="the directory in which the sound files reside",
        nargs=1)
# argument: table directory? table names? it would be nice to have some flexibility on this. Does Raven allow the specification of an output directory? This could get sloppy if the tables always go in the default Selections directory.
parser.add_argument("tables", 
        help="a list of selection tables to join into an SST",
        nargs="+")
# optional argument: output filename. If absent, print result to STDOUT.
parser.add_argument("-o", "--output_filename", nargs=1,
        help="the desired filename of the resulting SST. If not specified, \
                results are given on standard output")
# future argument: something about the filename format?! For now we assume that it is the default format.

args = parser.parse_args()
delim = "\t"


