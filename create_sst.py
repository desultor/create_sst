#!/usr/bin/env python

import csv
import argparse

parser = argparse.ArgumentParser(description="Create a Raven Sound Selection Table from batch detection tables")
# argument: table directory? table names? it would be nice to have some flexibility on this. Does Raven allow the specification of an output directory? This could get sloppy if the tables always go in the default Selections directory.
# argument: sound file directory (all must be in same directory. this is possibly a requirement of batch detection itself?)
# future argument: something about the filename format?! For now we assume that it is the default format.


