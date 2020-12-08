#!/bin/bash

usage(){
    echo -e "To call PLdataCleaner please use:"
    echo -e "$0 '<filepath>'"
    echo -e "-----"
}

FILEPATH=$1

if [[ "x$FILEPATH" == "x" ]]; then
    echo "Missing input file parameter. Exiting."
    usage
fi

FILENAME=$(basename "$FILEPATH")
DATALOC=$(dirname "$FILEPATH")

echo "Copying input file $FILEPATH to $DATALOC/temp_$FILENAME"
cp -a $FILEPATH $DATALOC/temp_$FILENAME

echo "Finding first line containing 'Grating 2=1800'..."
STARTLINE=$(grep -n "Grating 2=1800" $DATALOC/temp_$FILENAME | cut -f1 -d:)
STARTLINE=$(( $STARTLINE + 1 ))

echo "Removing the first $STARTLINE lines"
tail -n +$STARTLINE $DATALOC/temp_$FILENAME > $DATALOC/temp_$FILENAME.tmp && mv $DATALOC/temp_$FILENAME.tmp $DATALOC/temp_$FILENAME

echo "Merging columns and sorting according to column 1"
awk '{print $1"\t"$2"\n"$3"\t"$4}' $DATALOC/temp_$FILENAME | sort -k1 -n > $DATALOC/temp_$FILENAME.tmp && mv $DATALOC/temp_$FILENAME.tmp $DATALOC/temp_$FILENAME

echo "Substituting tabs with spaces. Resulting file in clean_${FILENAME}"
sed 's/\t/ /g' $DATALOC/temp_$FILENAME > $DATALOC/clean_$FILENAME

rm -r $DATALOC/temp_$FILENAME
