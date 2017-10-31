#run.sh
clear
echo "Starting Shell Script"
ls
cd \src
python -c 'import sys; print(sys.version_info[:])'
python sourcefile.py
echo "Shell Script Executed"
cat run.sh