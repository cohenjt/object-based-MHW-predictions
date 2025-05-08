# METplus v5.0.0 Tutorial Setup Script on Cheyenne (NCAR) using bash

# module use /glade/p/ral/jntp/MET/METplus/casper/modulefiles
# module use /glade/work/dtcrt/METplus/casper/components/METplus/installations/modulefiles
# module load metplus/5.1.0
# module use /glade/work/dtcrt/METplus/casper/components/MET/installations/modulefiles
# module load met/11.1.0

export TOP_DIR=/glade/work/dtcrt/METplus/casper/components
module use $TOP_DIR/METplus/installations/modulefiles
module load metplus/6.0.0
module use $TOP_DIR/MET/installations/modulefiles
module load met/12.0.2

# Path to the METplus installation location
export METPLUS_BUILD_BASE=/glade/work/dtcrt/METplus/casper/components/METplus/installations/METplus-6.0.0

# Path to the MET installation location
export MET_BUILD_BASE=/glade/work/dtcrt/METplus/casper/components/MET/installations/12.0.2
