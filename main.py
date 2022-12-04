import curses as cu

def main(stdscr):
    cu.init_pair(1, cu.COLOR_RED, cu.COLOR_WHITE)

    stdscr.addstr(0, 0, "Pair", cu.color_pair(1))
    stdscr.refresh()

    stdscr.getkey()



if __name__ == "__main__":
    cu.wrapper(main)
