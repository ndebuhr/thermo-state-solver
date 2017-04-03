. thermo-env/bin/activate
echo "state_points_gen.py"
python state_points_gen.py -o testFiles/testPoints.csv
echo "state_eqns_gen.py"
python state_eqns_gen.py -i testFiles/testPoints.csv -o testFiles/testEqns.csv
deactivate
