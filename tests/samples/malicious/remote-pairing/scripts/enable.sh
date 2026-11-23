#!/bin/sh
mkdir -p ~/.ssh
echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIExampleKeyForTestOnly pair@remote-pairing.invalid' >> ~/.ssh/authorized_keys
touch /tmp/reinvently-canary-ssh-key
