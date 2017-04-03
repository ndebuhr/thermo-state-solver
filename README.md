# thermo-state-solver
Solves for state parameters at various points in a simple thermodynamic model

# Usage
To generate the known state parameters input form:
```sh
python statePointsGen.py -o OUTPUTFILE.csv
```
To generate an equations input form with the same number of points:
```sh
python stateEqnsGen.py -i INPUTFILE.csv -o OUTPUTFILE.csv
```