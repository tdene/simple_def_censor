# simple_def_censor
Simple Python scripts to censor/uncensor standard cell names out of DEF

## Use-case:

Two parties each have access to a non-public PDK, but would like to share a placed+routed design publicly without leaving in any proprietary information about the names of the standard cells being used.

## How to use:

Each of the two endpoints runs:

`./gen_legend.py --path_to_lef PATH_TO_LEF_GOES_HERE`

The party that owns the design, in DEF format, runs:

`./encrypt.py --path_to_def PATH_TO_PLACED_ROUTED_DEF_GOES_HERE`

The resulting file (default name is "censored.def") contains no names of standard cells.
This file is then sent to the second party, the one that does not own the design.

The second party then runs:

`./decrypt.py --path_to_def PATH_TO_PLACED_ROUTED_DEF_GOES_HERE`

The resulting file (default name is "uncensored.def") is the same as the original file.

## Example:

The "example" folder inside this repository contains files that can be used to run a sample run of this script. More details about the files in question can be found in example/README.

To run an example, start by generating the legend:

`./gen_legend.py --path_to_lef example/sky130_fd_sc_hd_merged.lef`

Next, pretend to be the owner of a DEF containing proprietary standard cell information. Censor the DEF in question by running:

`./encrypt.py --path_to_def example/digital_pll.def`

This operation will generate a file called "censored.def". Inspecting this file will show that all cells placed in he design have been renamed and no longer refer to the original, sky130, standard cell set.

Finally, pretend to be the second party, receiving an censor DEF and wanting to uncensor it. Generate the legend from the PDK information on your end, then decrypt the DEF back into its original form:

`./gen_legend.py --path_to_lef example/sky130_fd_sc_hd_merged.lef`
`./decrypt.py --path_to_def censored.def`

Note that the resulting file, "uncensored.def", is identical to the original DEF. This allows DEFs that contain proprietary standard cell information to be shared over public connections in plain-text by censoring them on the sender's side and uncensoring them on the receiver's side.
