#!/bin/bash
FILENAME=$1

echo "This script filter-out unessary traffi"
currentDir=$(dirname "$(readlink -f "$0")")
pcapExtract="$currentDir/hourly"

if [ -d $pcapExtract ]
then
    rm -rf $pcapExtract/*
else
    mkdir -p $pcapExtract
fi
cd $currentDir
#echo $("pwd")
tshark -n -r 2014-04-07_capture-win13.short.pcap -q -z conv,udp,data -w $pcapExtract/newfile.pcap -F pcap
#editcap -i 86400 $pcapExtract/newfile.pcap output.pcap
