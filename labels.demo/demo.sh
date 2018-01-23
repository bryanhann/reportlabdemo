[ "$0" == "./demo.sh" ] || echo "try ./demo.sh"
[ "$0" == "./demo.sh" ] || exit
pyvenv tmp/pyvenv
source tmp/pyvenv/bin/activate
pip install -r pip.require
cd tmp
python ../main.py
open deleteme.pdf
cd ..
