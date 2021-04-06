#!/bin/python3

import argparse, sys

argparser=argparse.ArgumentParser()
argparser.add_argument("--path_to_def",type=str,default="censored.def",required=False)
argparser.add_argument("--legend",type=str,default="legend",required=False)
argparser.add_argument("--output",type=str,default="uncensored.def",required=False)

args=argparser.parse_args()

legend=eval(open(args.legend).read())
legend={b:a for a,b in legend.items()}

with open(args.path_to_def) as inp, open(args.output,'w') as out:
    started=False
    ended=False
    for line in inp:
        s=line.split()
        if started and len(s)>0 and s[0]=="END":
            ended=True

        if started and not ended:
            cell_name=s[2]
            print(line.replace(cell_name,legend[cell_name]),file=out,end='')
        else:
            print(line,file=out,end='')

        if not started and len(s)>0 and s[0]=="COMPONENTS":
            started=True
