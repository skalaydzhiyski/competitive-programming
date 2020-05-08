#!/bin/bash
mkdir $1;
cp solution-template/* "$1";
cd "$1";
echo Problem created { $1 }.
echo 'Hack away !'
