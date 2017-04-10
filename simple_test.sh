. thermo-env/bin/activate
echo "state_points_gen.py"
python state_points_gen.py -o testFiles/testPoints.csv -p 10
echo "state_eqns_gen.py"
python state_eqns_gen.py -i testFiles/testPoints.csv -o testFiles/testEqns.csv
deactivate

# TODO test output via a simple wc comparison
tenEqnWc=" 14  23 293 testEqns.csv"
tenPtsWc=" 6  6 40 testPoints.csv"
