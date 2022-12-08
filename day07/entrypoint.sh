#!/bin/sh
sed -E \
's/^\$ //; s/^cd \//dir aoc-tmp \&\& cd aoc-tmp/;'\
's/^ls//; s/dir (.+)/mkdir \1/;'\
's/^([0-9]+) (.+)/fallocate -l \1 \2/' /tmp/input.txt > /tmp/run.sh

sh /tmp/run.sh

find aoc-tmp -type d -exec sh -c \
'p="$1"; du -b "$p" | awk '"'END{print \$1 - NR * 4096}'"'' shell {} \; \
| sort -rn \
| awk 'BEGIN{getline need; need -= 40000000}; '\
'{if ($1 >= need) {ans = $1}; '\
'if ($1 <= 100000) {sum += $1}}; END {print "1: " sum "\n2: " ans}'
