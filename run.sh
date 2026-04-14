#!/bin/bash
for user in $(cat users.txt)
do
  python -m ofscraper --user $user
done
