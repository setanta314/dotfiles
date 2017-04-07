#!/usr/bin/env python3

import curses
import os
import sys


BOOKMARK_FILE = os.path.expanduser("~/.config/ranger/bookmarks")


def print_stderr(string):
    sys.stderr.write(string)
    sys.stderr.flush()


def main(stdscr):
    if not os.path.exists(BOOKMARK_FILE):
        print_stderr("could not find bookmark file")
        return 1

    bookmarks = {}
    current_pos = 0
    with open(BOOKMARK_FILE) as f:
        for line in f.readlines():
            key, path = line.split(":")
            bookmarks[key] = path.strip()
    keys = sorted(bookmarks.keys())

    while True:
        # refresh display
        stdscr.clear()
        for i, key in enumerate(keys):
            path = bookmarks[key]
            if i == current_pos:
                stdscr.addstr(
                    current_pos,
                    0,
                    '{} => {}'.format(key, path),
                    curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, '{} => {}'.format(key, path))
        stdscr.refresh()

        c = stdscr.getkey()
        if c in keys:
            sys.stderr.write
            print_stderr(bookmarks[c])
            return 0

        if c == 'KEY_DOWN':
            current_pos += 1
        elif c == 'KEY_UP':
            current_pos -= 1
        elif c == '\n':
            print_stderr(bookmarks[keys[current_pos]])
            return 0
        current_pos %= len(keys)

curses.wrapper(main)
