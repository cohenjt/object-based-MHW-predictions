#!/bin/bash -l
### Job Name
#PBS -N run_mode_array_R3
### Charging account
#PBS -A UWIS0040
### Request one chunk of resources with 1 CPU and 10 GB of memory
#PBS -l select=1:ncpus=1:mem=4GB
### Allow job to run up to 15 hours
#PBS -l walltime=6:00:00
### Route the job to the casper queue
#PBS -q casper
### Run MODE from 1989-2018
#PBS -J 1989-2018
### Join output and error streams into single file
#PBS -j oe
### Set email
#PBS -m abe
#PBS -M jtcohen@uw.edu

### Load Python module and activate NPL environment
module load conda
conda activate /glade/work/jtcohen/envs

### set up MODE
source MODE_setup.sh

### Run analysis script
run_metplus.py -c year_conf_files/MODE_mhw_${PBS_ARRAY_INDEX}.conf -c MODE_mhw_settings_R3.conf