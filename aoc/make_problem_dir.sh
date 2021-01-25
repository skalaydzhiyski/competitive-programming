#!/bin/bash
mkdir "$1";
cd "$1";
touch input;
touch run_solution.py;
echo '#!/usr/bin/python3' > run_solution.py;
chmod +x run_solution.py;
echo 'done.'

