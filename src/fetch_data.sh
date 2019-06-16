#!/usr/bin/env bash

set -exu

base_dir=/mnt/maple/kawahara/WWW.en/select3/txt_uniq
for (( i = 0; i < 10800; ++i )); do
    number=$(printf "%05d" ${i})
    file_path=${base_dir}/${number}.txt.gz
    if [[ $(gzcat -f ${file_path} | wc -l) -gt 100 ]]; then
        gzcat ${file_path} | shuf | tee >(head -n 90 >> train.txt) | tail -n 10 >> test.txt
    fi
done
