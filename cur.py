import curses
# from curses import wrapper 

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.getch()
    
curses.wrapper(main)