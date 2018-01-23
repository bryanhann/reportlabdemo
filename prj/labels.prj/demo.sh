[ "$0" == "./demo.sh" ] || echo "try ./demo.sh"
[ "$0" == "./demo.sh" ] || exit
pyvenv tmp/pyvenv
source tmp/pyvenv/bin/activate
pip install -r src/pip.require
cd tmp
python ../src/main.py
open deleteme.pdf
cd ..
