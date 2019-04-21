#! /bin/bash
# Author: Tanner Glantz
# Title: file_attribution_script (fas)

echo "* ----------------------------*"
echo "|    File Attribution Script  |"
echo "* ----------------------------*"
echo ""
echo "WARNING: Program doesn't detect if input is a valid file."
echo ""

if [ $# = 1 ]
then
	if [ $1 == "-h" ] 
	then
		# help menu if "-h" switch is provided
		echo "sas.sh is written by Tanner Glantz. Project utilizes the ssdeep tool and tlsh tool."
		echo "./sas.sh [File A] [File B]"
		exit 1
	fi
fi


if [ $# -gt 1 -a $# -lt 3 ]
then
	echo "-> Running [ssdeep] to check for similarity between files ($1) and ($2)."
	ssdeep $1 $2 > ssdeep_comparison
	echo ""
	python parse_ssdeep_output.py
	echo ""
	echo "-> Running [sdhash] to check for similarity between files ($1) and ($2)."
	echo ""
	sdhash $1 > sdhash_filea
	sdhash $2 > sdhash_fileb
	sdhash -c sdhash_filea sdhash_fileb > sdhash_results
	python parse_sdhash_output.py

	echo " Using [diff] to point out line diffrences for better context"
	echo ""
	echo "------------"
	echo "DIFF  OUTPUT"
	echo "------------"
	diff $1 $2
	
else
	echo "Error. Invalid Command Line Args."
fi

