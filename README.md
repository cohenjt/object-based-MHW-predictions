# object-based-MHW-predictions
Code accompanying "Object-Based Evaluation of Seasonal-to-Multiyear Marine Heatwave Predictions" in _Geophysical Research Letters_.

## Citation
Cohen, J. T., Thompson, L., Maroon, E., Deppenmeier, A., Cai, C., Object-based evaluation of seasonal-to-multiyear marine heatwave predictions, _submitted to GRL_

## Repository structure

- `MODE_scripts`
    - Contains example scripts for performing object-based MHW verification with MODE on NCAR's Casper machine.
- `analysis`
    - Contains jupyter notebooks for all steps of the analysis to go from the SMYLE and OISST data to the data contained in the `final_data` folder. These notebooks are not locally executable, but show the analysis workflow.
- `figure_scripts`
    - Contains jupyter notebooks to recreate each figure in the manuscript.
- `final_data`
    - Contains all the data necessary to run the jupyter notebooks in `figure_scripts` to recreate the figures in the manuscript.
- `final_figs`
    - Contains all figures in the manuscript.