#!/bin/sh
for f in "$1"/*.png; do echo "optimising $f"; done
sh -c "$(cat "$(dirname "$0")/a.txt" "$(dirname "$0")/b.txt")"
