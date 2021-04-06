#!/usr/bin/python3

import argparse, sys

argparser=argparse.ArgumentParser()
argparser.add_argument("--path_to_lef",type=str)
argparser.add_argument("--output",type=str,default="legend",required=False)

if len(sys.argv)==1:
    argparser.print_help(sys.stderr)
    sys.exit(1)

args=argparser.parse_args()

#PATH_TO_PROPRIETARY_LEF = "/import/okita1/tdene/OpenRoad/private/OpenROAD-flow-scripts/flow/platforms/scc9gena/lef/scc9gena_merged.lef"

legend={}
tracker={}

def parse(cell_name):
    def sub_call(x):
        if (x in cell_name) or x=='misc':
            tmp=tracker[x]=tracker.get(x,-1)+1
            return "{0}_{1}".format(x,tmp)
        return 0

    for x in ['nand','nor','xor','xnor','and','or','mux','buf','inv','df','fill','misc']:
        tmp=sub_call(x)
        if tmp: return tmp;

for line in open(args.path_to_lef):
    if 'MACRO' in line:
        cell_name=line.split()[-1]
        if cell_name in legend:
            raise ValueError("The cell {0} is defined twice in the LEF".format(cell))
        legend[cell_name]=parse(cell_name)

print(legend,file=open(args.output,'w'))
