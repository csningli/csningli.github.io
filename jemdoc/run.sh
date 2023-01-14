#! /bin/bash

CONENV="python27"

CONCON=$(which conda)
CONBIN=${CONCON%/*}
CONPATH=${CONBIN%/*}

OUT=$(conda --version)
VER=${OUT#*\ }
PRI_SEC=${VER%\.*}
PRI=${PRI_SEC%%\.*}
SEC=${PRI_SEC##*\.}

if [ $PRI -lt 5 ] && [ $SEC -lt 4 ]
then
  source activate $CONENV
else
  source $CONPATH"/etc/profile.d/conda.sh"
  conda deactivate
  conda activate $CONENV
fi

for PAGE in index bio teaching news problems group pubs patents ;
do
  python jemdoc.py $PAGE
  mv $PAGE.html ../$PAGE.html
done
