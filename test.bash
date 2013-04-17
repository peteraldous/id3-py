#!/bin/bash
diff <(python test_script.py) <(python3 test_script.py)
if [ 0 -eq $? ]; then
  echo "test passed";
else
  echo "test failed";
fi
