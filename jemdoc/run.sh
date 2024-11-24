#! /bin/bash

CONENV="jemdoc"

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

for NAME in index news posts ;
do
  python jemdoc.py $NAME
  mv $NAME.html ../$NAME.html
done

for PAGE in posts/*.jemdoc ;
do
  python jemdoc.py $PAGE
  NAME=${PAGE%.jemdoc}
  mv $NAME.html ../$NAME.html
done
