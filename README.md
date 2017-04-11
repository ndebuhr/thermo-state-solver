# thermo-state-solver
Solves for state parameters at various points in a simple thermodynamic model

# Usage
To generate the known state parameters input form (with number of points in system being ##):
```sh
python statePointsGen.py -o OUTPUTFILE.csv -p \#\#
```
To generate an equations input form with the same number of points:
```sh
python stateEqnsGen.py -i INPUTFILE.csv -o OUTPUTFILE.csv
```