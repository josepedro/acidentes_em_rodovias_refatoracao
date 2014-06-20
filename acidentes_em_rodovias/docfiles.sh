#!/bin/bash


echo -n 'Running Doxygen ... '
doxygen Doxyfile
echo 'Done'

#echo -n 'Running Epydoc ... '
#epydoc --html -o ../../Documents/epydoc/ --parse-only -q --name Acidentes_Rodovias --graph all --docformat plaintext app
#echo 'Done'

echo -n 'Running Pylint ... '
pylint app --output-format=html --ignore=tests> ../../Documents/pylint.html
pylint app > ../../Documents/pylint.log
echo 'Done'

echo -n 'Generating graphs ... '
pyreverse -o png app -p Acidentes_Rodovias -f ALL > pyreverse.log
mv *.png ../../Documents/
echo 'Done'