#!/bin/bash
for printer in `lpstat -p | awk '{print $2}'`
do
echo Deleting $printer
lpadmin -x $printer
done
echo "Adding printers"
mkdir /opt/printers
wget http://mirrors/printers/canon/CNADVC3325X1.PPD
mv CNADVC3325X1.PPD /opt/printers/
lpadmin -p Galaxy -L 'Galaxy' -P /opt/printers/CNADVC3325X1.PPD -v socket://10.0.0.42 -E -o media=letter -o printer-is-shared=false
lpadmin -p Admin -L 'Admin' -P /opt/printers/CNADVC3325X1.PPD -v socket://10.0.0.40 -E -o media=letter -o printer-is-shared=false
lpadmin -p Manufacturing -L 'Manufacturing' -P /opt/printers/CNADVC3325X1.PPD -v socket://10.0.0.39 -E -o media=letter -o printer-is-shared=false
lpadmin -d Galaxy
