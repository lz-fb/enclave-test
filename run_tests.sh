# Runs all files matching test_*.py

for t in test_*.py
  do
  python3 $t &
  done
