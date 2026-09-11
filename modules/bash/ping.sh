#!/bin/bash
target=$1

if [[ "$(uname -s)" == "Linux" ]]; then
    ping -c 4 "$target"
else
    ping -n 4 "$target"
fi