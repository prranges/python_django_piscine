#!/bin/sh

if [ $1 ]; then
curl -s -I $1 | grep Location | cut -f2 -d ' '
fi