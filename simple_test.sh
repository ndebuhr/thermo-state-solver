#!/usr/bin/env bash

. thermo-env/bin/activate

# TODO extend beyond 9 points, improve functionality, improve test case variability, clean up messy code
# Single digit number of points test
echo "----------Number of Points Test----------"
for i in $(seq 1 1 9)
do
    echo "state_points_gen.py"
    python state_points_gen.py -o testFiles/testPoints.csv -p $i
    # cat testFiles/testPoints.csv | wc
    ptsWc=$(cat testFiles/testPoints.csv | wc)
    ptsLines=$(echo $ptsWc | sed 's/\s*[0-9]*\s*[0-9]*\s*$//g' )
    ptsWords=$(echo $ptsWc | sed 's/^\s*[0-9]*\s*//g' | sed 's/\s*[0-9]*\s*$//g' )
    ptsBytes=$(echo $ptsWc | sed 's/^\s*[0-9]*\s*[0-9]*\s*//g' )
    echo "$ptsLines Lines, $ptsWords Words, $ptsBytes Bytes"
    if (($ptsLines != 6))
    then
	echo "Test case of points csv generation, for $i points, resulted in $ptsLines != 6 lines"
	exit 0
    fi
    if (($ptsWords != 6))
    then
	echo "Test case of points csv generation, for $i points, resulted in $ptsWords != 6 words"
	exit 0
    fi
    ptsBytesExpect=20+2*$i
    if (($ptsBytes != $ptsBytesExpect))
    then
	echo "Test case of points csv generation, for $i points, resulted in $ptsBytes != $ptsBytesExpect bytes"
	exit 0	
    fi
    
    echo "state_eqns_gen.py"
    python state_eqns_gen.py -i testFiles/testPoints.csv -o testFiles/testEqns.csv
    # cat testFiles/testEqns.csv | wc
    eqnsWc=$(cat testFiles/testEqns.csv | wc)
    eqnsLines=$(echo $eqnsWc | sed 's/\s*[0-9]*\s*[0-9]*\s*$//g' )
    eqnsWords=$(echo $eqnsWc | sed 's/^\s*[0-9]*\s*//g' | sed 's/\s*[0-9]*\s*$//g' )
    eqnsBytes=$(echo $eqnsWc | sed 's/^\s*[0-9]*\s*[0-9]*\s*//g' )
    echo "$eqnsLines Lines, $eqnsWords Words, $eqnsBytes Bytes"
    eqnsLinesExpect=4+$i
    if (($eqnsLines != $eqnsLinesExpect))
    then
	echo "Test case of equations csv generation, for $i points, resulted in $eqnsLines != $eqnsLinesExpect lines"
	exit 0
    fi
    eqnsWordsExpect=3+2*$i
    if (($eqnsWords != $eqnsWordsExpect))
    then
	echo "Test case of equations csv generation, for $i points, resulted in $eqnsWords != $eqnsWordsExpect words"
	exit 0
    fi
    eqnsBytesExpect=51+24*$i
    if (($eqnsBytes != $eqnsBytesExpect))
    then
	echo "Test case of equations csv generation, for $i points, resulted in $eqnsBytes != $eqnsBytesExpect bytes"
	exit 0	
    fi
    echo ""
    
done

rm testFiles/testEqns.csv
rm testFiles/testPoints.csv


# File naming test
randLen=0
while [ $randLen -ne 5 ] # runs test a random number of times. 1/10 chance for test to end each iteration
do
    randLen=$(( ( RANDOM % 10 ) + 1 )) # non-uniform, but okay
    echo "----------File Naming Test----------"
    dictWc=$(wc /usr/share/dict/words)
    dictLines=$(echo $dictWc | sed 's/\(^[0-9]*\).*/\1/g' )
    randLineOne=$(( ( RANDOM * RANDOM % $dictLines ) + 1 )) # Very non-uniform/biased, but that's okay for now
    randLineTwo=$(( ( RANDOM * RANDOM % $dictLines ) + 1 )) # Very non-uniform/biased, but that's okay for now
    fileNameOne=$(head -n $randLineOne /usr/share/dict/words | tail -n 1)
    fileNameTwo=$(head -n $randLineTwo /usr/share/dict/words | tail -n 1)
    echo "state_points_gen.py"
    python state_points_gen.py -o "testFiles/$fileNameOne.csv" -p 15
    echo "state_eqns_gen.py"
    python state_eqns_gen.py -i "testFiles/$fileNameOne.csv" -o "testFiles/$fileNameTwo.csv"
    echo ""
    if test -e "testFiles/$fileNameOne.csv";
    then
	rm "testFiles/$fileNameOne.csv"
    else
	echo "File naming test failed. $fileNameOne.csv does not exit."
	exit 0
    fi
    if test -e "testFiles/$fileNameTwo.csv";
    then
	rm "testFiles/$fileNameTwo.csv"
    else
	echo "File naming test failed. $fileNameTwo.csv does not exit."
	exit 0
    fi
done

cntTestFiles=$(ls testFiles/ | wc)
numTestFiles=$(echo $cntTestFiles | sed 's/[0-9]*\s*[0-9]*\s*$//g')
if [ $numTestFiles -gt 2 ];
then
    echo "More than 2 files in test files directory"
fi

deactivate

