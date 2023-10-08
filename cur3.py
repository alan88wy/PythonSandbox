# demo-window-border.py

import curses
import math
import sys

def main(argv):
  # BEGIN ncurses startup/initialization...
  # Initialize the curses object.
  stdscr = curses.initscr()

  # Do not echo keys back to the client.
  curses.noecho()

  # Non-blocking or cbreak mode... do not wait for Enter key to be pressed.
  curses.cbreak()

  # Turn off blinking cursor
  curses.curs_set(False)

  # Enable color if we can...
  if curses.has_colors():
    curses.start_color()

  # Optional - Enable the keypad. This also decodes multi-byte key sequences
  # stdscr.keypad(True)

  # END ncurses startup/initialization...

  caughtExceptions = ""
  try:
   # Create a 5x5 window in the center of the terminal window, and then
   # alternate displaying a border and not on each key press.

   # We don't need to know where the approximate center of the terminal
   # is, but we do need to use the curses terminal size constants to
   # calculate the X, Y coordinates of where we can place the window in
   # order for it to be roughly centered.
   topMostY = math.floor((curses.LINES - 5)/2)
   leftMostX = math.floor((curses.COLS - 5)/2)

   # Place a caption at the bottom left of the terminal indicating 
   # action keys.
   stdscr.addstr (curses.LINES-1, 0, "Press Q to quit, any other key to alternate.")
   stdscr.refresh()
   
   # We're just using white on red for the window here:
   curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)

   index = 0
   done = False
   while False == done:
    # If we're on the first iteration, let's skip straight to creating the window.
    if 0 != index:
     # Grabs a value from the keyboard without Enter having to be pressed. 
     ch = stdscr.getch()
     # Need to match on both upper-case or lower-case Q:
     if ch == ord('Q') or ch == ord('q'): 
      done = True
    mainWindow = curses.newwin(5, 5, topMostY, leftMostX)
    mainWindow.bkgd(' ', curses.color_pair(1))
    if 0 == index % 2:
     mainWindow.box()
    else:
     # There's no way to "unbox," so blank out the border instead.
     mainWindow.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    mainWindow.refresh()

    stdscr.addstr(0, 0, "Iteration [" + str(index) + "]")
    stdscr.refresh()
    index = 1 + index

  except Exception as err:
   # Just printing from here will not work, as the program is still set to
   # use ncurses.
   # print ("Some error [" + str(err) + "] occurred.")
   caughtExceptions = str(err)

  # BEGIN ncurses shutdown/deinitialization...
  # Turn off cbreak mode...
  curses.nocbreak()

  # Turn echo back on.
  curses.echo()

  # Restore cursor blinking.
  curses.curs_set(True)

  # Turn off the keypad...
  # stdscr.keypad(False)

  # Restore Terminal to original state.
  curses.endwin()

  # END ncurses shutdown/deinitialization...

  # Display Errors if any happened:
  if "" != caughtExceptions:
   print ("Got error(s) [" + caughtExceptions + "]")

if __name__ == "__main__":
  main(sys.argv[1:])