dir_name="day$(date +%d)"
mkdir -p $dir_name
aocd > $dir_name/input.txt
touch $dir_name/test.txt
cp template.py  $dir_name/solution.py
cp template.md  $dir_name/README.md
code .