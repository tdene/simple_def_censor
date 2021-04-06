# simple_def_censor
Simple Python scripts to censor/uncensor standard cell names out of DEF

## Use-case:

Two parties each have access to a non-public PDK, but would like to share a placed+routed design publicly without leaving in any proprietary information about the names of the standard cells being used.

## How to use:

Each of the two endpoints runs:
`./gen_legend.py --path_to_lef PATH_TO_LEF_GOES_HERE`

The party that owns the design, in DEF format, runs:
`./encrypt --path_to_def PATH_TO_PLACED_ROUTED_DEF_GOES_HERE`

The resulting file (default name is "censored.def") contains no names of standard cells.
This file is then sent to the second party, the one that does not own the design.

The second party then runs:
`./decrypt --path_to_def PATH_TO_PLACED_ROUTED_DEF_GOES_HERE`

The resulting file (default name is "uncensored.def") is the same as the original file.
