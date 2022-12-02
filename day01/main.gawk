# awk -f day01/main.gawk day01/input.txt
function set_max(){ max[4] = sum; asort(max, max, "@val_num_desc"); sum = 0 }
{ (NF) ? sum += $1 : set_max() }
END { set_max(); printf "1: %d\n2: %d\n", max[1], max[1]+max[2]+max[3] }
