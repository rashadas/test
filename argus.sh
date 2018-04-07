#!/bin/bash
FILES=/home/rashad/brett_dumps/botnets/storm/*

for f in $FILES
do
  #echo "Processing $f file..."
  hexdump -n 4 -C $f | cut -c 10-21 | grep "d4 c3 b2 a1" > /dev/null && argus -r $f -F /etc/argus.conf -w $f.biargus && ra -n -Z b -F /etc
/ra.conf -r $f.biargus > $f.binetflow
  # take action on each file. $f store current file name
  #result=$(hexdump -n 4 -C $f | cut -c 10-21)
done
