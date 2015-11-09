#!/usr/bin/env python
# encoding: utf-8

import sys

# how many spaces between each column
PADDING = 3
# extra padding added inside each column on right
OVERHANG = 2

def main():
    out_lines = list()
    in_lines = sys.stdin.readlines()
    if in_lines:
        out_lines = process(in_lines)
    sys.stdout.writelines(out_lines)
    sys.stdout.flush()

def process(in_lines):
    out_lines = remove_cr(in_lines)
    out_lines = read(out_lines)
    out_lines = strip_whitespace(out_lines)
    out_lines = add_missing_cols(out_lines)
    max_lens = find_max_lens(out_lines)
    out_lines = write_pandoc(out_lines, max_lens)
    return out_lines

def remove_cr(in_lines):
    out_lines = [j.strip() for j in in_lines]
    return out_lines

def read(in_lines):
    out_lines = [j.split('\t') for j in in_lines]
    return out_lines

def strip_whitespace(in_lines):
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

def find_max_lens(in_lines):
    max_lens = [1] * len(in_lines[0])
    for j in in_lines:
        for n, i in enumerate(j):
            max_lens[n] = max(max_lens[n], len(i))
    # add overhang to each column
    max_lens = [i + OVERHANG for i in max_lens]
    return max_lens

def write_pandoc(in_lines, max_lens):
    # write pandoc-style tables
    # http://pandoc.org/README.html#tables

    def pad_cells(in_lines, max_lens):
        out_lines = list()
        for j in in_lines:
            out = [str(i).ljust(max_lens[n]) for n, i in enumerate(j)]
            out_lines.append(out)
        return out_lines

    def delimit_start_end(in_lines, max_lens):
        # add delimiters for pandoc tables
        d = ['-' * n for n in max_lens]
        out_lines = [d] + in_lines + [d]
        return out_lines

    def rejoin(in_lines):
        sep = ' ' * PADDING
        out_lines = [sep.join(j) + '\n' for j in in_lines]
        return out_lines

    out_lines = pad_cells(in_lines, max_lens)
    out_lines = delimit_start_end(out_lines, max_lens)
    out_lines = rejoin(out_lines)
    return out_lines

if __name__ == '__main__':
    main()
