#run.sh
clear
echo "Starting Shell Script"
ls
cd \src
echo "Python Version"
python -c 'import sys; print(sys.version_info[:])'
pip -V
pip install numpy
python sourcefile.py
echo "Shell Script Executed"
cat run.sh