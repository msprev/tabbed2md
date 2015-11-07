#!/usr/bin/env python
# encoding: utf-8

import sys

# how many spaces between each column
PADDING = 3

def main():
    in_lines = sys.stdin.readlines()
    out_lines = process(in_lines)
    if out_lines:
        sys.stdout.writelines(out_lines)
        sys.stdout.flush()

def process(in_lines):
    out_lines = remove_cr(in_lines)
    out_lines = split_by_col(out_lines)
    out_lines = remove_whitespace(out_lines)
    out_lines = add_missing_cols(out_lines)
    max_lens = find_max_entries(out_lines)
    out_lines = add_spaces(out_lines, max_lens)
    out_lines = delimit_pandoc(out_lines, max_lens)
    out_lines = rejoin(out_lines)
    return out_lines

def remove_cr(in_lines):
    out_lines = [j.strip() for j in in_lines]
    return out_lines

def split_by_col(in_lines):
    out_lines = [j.split('\t') for j in in_lines]
    return out_lines

def remove_whitespace(in_lines):
    out_lines = [[i.strip() for i in j] for j in in_lines]
    return out_lines

def add_missing_cols(in_lines):
    max_cols = max([len(j) for j in in_lines])
    out_lines = list()
    for j in in_lines:
        out = j
        missing = max_cols - len(j)
        out.extend([''] * missing)
        out_lines.append(out)
    return out_lines

def find_max_entries(in_lines):
    # start building a dict as it's easier to add new elements in middle
    max_lens = dict()
    for j in in_lines:
        for n, i in enumerate(j):
            current = max_lens.get(n, 0)
            max_lens[n] = max(current, len(i))
    # convert dict to a list...
    l = [0] * len(max_lens)
    for key in max_lens:
        l[key] = max_lens[key]
    return l

def add_spaces(in_lines, max_lens):
    out_lines = list()
    for j in in_lines:
        out = [str(i).ljust(max_lens[n]) for n, i in enumerate(j)]
        out_lines.append(out)
    return out_lines

def delimit_pandoc(in_lines, max_lens):
    # add delimiters for pandoc tables
    d = ['-' * n for n in max_lens]
    out_lines = [d] + in_lines + [d]
    return out_lines

def rejoin(in_lines):
    sep = ' ' * PADDING
    out_lines = [sep.join(j) + '\n' for j in in_lines]
    return out_lines

if __name__ == '__main__':
    main()
