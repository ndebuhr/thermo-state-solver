. thermo-env/bin/activate

for i in $(seq 1 1 20)
do
    echo "state_points_gen.py"
    python state_points_gen.py -o testFiles/testPoints.csv -p $i
    # cat testFiles/testPoints.csv | wc
    ptsWc=$(cat testFiles/testPoints.csv | wc)
    ptsLines=$(echo $ptsWc | sed 's/\s*[0-9]*\s*[0-9]*\s*$//g' )
    ptsWords=$(echo $ptsWc | sed 's/^\s*[0-9]*\s*//g' | sed 's/\s*[0-9]*\s*$//g' )
    ptsBytes=$(echo $ptsWc | sed 's/^\s*[0-9]*\s*[0-9]*\s*//g' )
    echo "$ptsLines Lines, $ptsWords Words, $ptsBytes Bytes"
    # TODO - complete below
    # if (($ptsLines != 6))
    #    failed="Test case of points csv generation, for $i points, resulted in $ptsLines != 6 lines"
    # if (($ptsLines != 6))
    #    failed="Test case of points csv generation, for $i points, resulted in $ptsLines != 6 lines"
    # if (($ptsLines != 6))
    #    failed="Test case of points csv generation, for $i points, resulted in $ptsLines != 6 lines"       

    echo "state_eqns_gen.py"
    python state_eqns_gen.py -i testFiles/testPoints.csv -o testFiles/testEqns.csv
    # cat testFiles/testEqns.csv | wc
    eqnsWc=$(cat testFiles/testEqns.csv | wc)
    eqnsLines=$(echo $eqnsWc | sed 's/\s*[0-9]*\s*[0-9]*\s*$//g' )
    eqnsWords=$(echo $eqnsWc | sed 's/^\s*[0-9]*\s*//g' | sed 's/\s*[0-9]*\s*$//g' )
    eqnsBytes=$(echo $eqnsWc | sed 's/^\s*[0-9]*\s*[0-9]*\s*//g' )
    echo "$eqnsLines Lines, $eqnsWords Words, $eqnsBytes Bytes"
    echo ""
    
done

deactivate




# TODO test output via a simple wc comparison
tenEqnWc=" 14  23 293 testEqns.csv"
tenPtsWc=" 6  6 40 testPoints.csv"
