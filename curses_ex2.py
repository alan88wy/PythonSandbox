# Uses the curses library to create 3 randomly sized windows with different color
# backgrounds on the screen.

# Note that this is not the most efficient way to code this, but I want to break out
# the individual objects so that it is easier to trace what is going on.

import curses
import math
import random
import sys

# A set of layouts, to be randomly chosen.
layouts = ['2 top, 1 bottom', '2 left, 1 right',
          '1 top, 2 bottom', '1 left, 2 right']


def main(argv):
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

    # Beginning of Program...
    # Create a list of all the colors except for black and white. These will server as
    # the background colors for the windows. Because these constants are defined in
    # ncurses,
    # we can't create the list until after the curses.initscr call:
    bgColors = [curses.COLOR_BLUE, curses.COLOR_CYAN, curses.COLOR_GREEN,
                curses.COLOR_MAGENTA, curses.COLOR_RED, curses.COLOR_YELLOW]
    colors = random.sample(bgColors, 3)

    # Create 3 ncurses color pair objects.
    curses.init_pair(1, curses.COLOR_WHITE, colors[0])
    curses.init_pair(2, curses.COLOR_WHITE, colors[1])
    curses.init_pair(3, curses.COLOR_WHITE, colors[2])

    caughtExceptions = ""

    try:
        # Note that print statements do not work when using ncurses. If you want to write
        # to the terminal outside of a window, use the stdscr.addstr method and specify
        # where the text will go. Then use the stdscr.refresh method to refresh the
        # display.
        # stdscr.addstr(0, 0, "Gonna make some windows.")
        # stdscr.refresh()

        # The lists below will eventually hold 4 values, the X and Y coordinates of the
        # top-left corner relative to the screen itself, and the number of characters
        # going right and down, respectively.
        # window1 = []
        # window2 = []
        # window3 = []

        # The variables below will eventually contain the window objects.
        window1Obj = ""
        window2Obj = ""
        window3Obj = ""

        # The variables below will correspond roughly to the X, Y coordinates of the
        # of each window.
        window1 = []
        window2 = []
        window3 = []

        # There's going to be a caption at the bottom left of the screen, but it needs to
        # go in the proper window.
        window1Caption = ""
        window2Caption = ""
        window3Caption = ""

        # The randomly sized windows that don't take up one side of the screen shouldn't
        # be less than 1/3 the screen size, or more than one third of the screen size on
        # either edge.
        minWindowWidth = math.floor(curses.COLS * 1.0/3.0)
        maxWindowWidth = math.floor(curses.COLS * 2.0/3.0)
        minWindowHeight = math.floor(curses.LINES * 1.0/3.0)
        maxWindowHeight = math.floor(curses.LINES * 2.0/3.0)

        # Pick a layout. The random.randrange command will return a value between 0 and 3.
        chosenLayout = layouts[random.randrange(0, 4)]

        if '2 top, 1 bottom' == chosenLayout:
            # Windows 1 and 2 will be the top, Window 3 will be the bottom.
            window1Width = random.randrange(minWindowWidth, maxWindowWidth)
            window1Height = random.randrange(minWindowHeight, maxWindowHeight)
            window1 = [0, 0, window1Width, window1Height]

            window2Width = curses.COLS - window1Width
            window2Height = window1Height
            window2 = [window1Width, 0, window2Width, window2Height]

            window3 = [0, window1Height, curses.COLS,
                      curses.LINES - window1Height]
            window3Caption = chosenLayout + " - Press a key to quit."

        elif '2 left, 1 right' == chosenLayout:
            # Windows 1 and 2 will be on the left, Window 3 will be on the right.
            window1Width = random.randrange(minWindowWidth, maxWindowWidth)
            window1Height = random.randrange(minWindowHeight, maxWindowHeight)
            window1 = [0, 0, window1Width, window1Height]

            window2Width = window1Width
            window2Height = curses.LINES - window1Height
            window2 = [0, window1Height, window2Width, window2Height]
            window2Caption = chosenLayout + " - Press a key to quit."

            window3Width = curses.COLS - window1Width
            window3Height = curses.LINES
            window3 = [window1Width, 0, window3Width, window3Height]

        elif '1 top, 2 bottom' == chosenLayout:
            # Window 1 will be on the top, Windows 2 and 3 will be on the bottom.
            window1Width = curses.COLS
            window1Height = random.randrange(minWindowHeight, maxWindowHeight)
            window1 = [0, 0, window1Width, window1Height]

            window2Width = random.randrange(minWindowWidth, maxWindowWidth)
            window2Height = curses.LINES - window1Height
            window2 = [0, window1Height, window2Width, window2Height]
            window2Caption = chosenLayout + " - Press a key to quit."

            window3Width = curses.COLS - window2Width
            window3Height = window2Height
            window3 = [window2Width, window1Height,
                      window3Width, window3Height]

        elif '1 left, 2 right' == chosenLayout:
            # Window 1 will be on the left, Windows 2 and 3 will be on the right.
            window1Width = random.randrange(minWindowWidth, maxWindowWidth)
            window1Height = curses.LINES
            window1 = [0, 0, window1Width, window1Height]
            window1Caption = chosenLayout + " - Press a key to quit."

            window2Width = curses.COLS - window1Width
            window2Height = random.randrange(minWindowHeight, maxWindowHeight)
            window2 = [window1Width, 0, window2Width, window2Height]

            window3Width = window2Width
            window3Height = curses.LINES - window2Height
            window3 = [window1Width, window2Height,
                      window3Width, window3Height]

        # Create and refresh each window. Put the caption 2 lines up from bottom
        # in case it wraps. Putting it on the last line with no room to wrap (if
        # the window is too narrow for the text) will cause an exception.

        # The newwin() function creates a new window of a given size, returning the new window object.
        
        window1Obj = curses.newwin(
            window1[3], window1[2], window1[1], window1[0])
        
        # window.bkgd(ch[, attr])
        # Set the background property of the window to the character ch, with attributes attr. The change
        # is then applied to every character position in that window:
        #   * The attribute of every character in the window is changed to the new background attribute.
        #   * Wherever the former background character appears, it is changed to the new background character.
        window1Obj.bkgd(' ', curses.color_pair(1))
        
        # Calculate rough center...
        window1Center = [math.floor(window1[2]/2.0),
                        math.floor(window1[3]/2.0)]
        # Add the string to the center, with BOLD flavoring.
        window1Obj.addstr(window1Center[1], window1Center[0] - 4, "Window 1",
                          curses.color_pair(1) | curses.A_BOLD)
        if "" != window1Caption:
            window1Obj.addstr(curses.LINES - 2, 0, window1Caption,
                              curses.color_pair(1) | curses.A_BOLD)
        window1Obj.refresh()

        window2Obj = curses.newwin(
            window2[3], window2[2], window2[1], window2[0])
        window2Obj.bkgd(' ', curses.color_pair(2))
        # Calculate rough center...
        window2Center = [math.floor(window2[2]/2.0),
                        math.floor(window2[3]/2.0)]
        # Add the string to the center, with BOLD flavoring.
        window2Obj.addstr(window2Center[1], window2Center[0] - 4, "Window 2",
                          curses.color_pair(2) | curses.A_BOLD)
        if "" != window2Caption:
            # The "Y coordinate" here is the bottom of the *window* and not the screen.
            window2Obj.addstr(window2[3] - 2, 0, window2Caption,
                              curses.color_pair(2) | curses.A_BOLD)
        window2Obj.refresh()

        window3Obj = curses.newwin(
            window3[3], window3[2], window3[1], window3[0])
        window3Obj.bkgd(' ', curses.color_pair(3))
        # Calculate rough center...
        window3Center = [math.floor(window3[2]/2.0),
                        math.floor(window3[3]/2.0)]
        # Add the string to the center, with BOLD flavoring.
        window3Obj.addstr(window3Center[1], window3Center[0] - 4, "Window 3",
                          curses.color_pair(3) | curses.A_BOLD)
        if "" != window3Caption:
            # The "Y coordinate" here is the bottom of the *window* and not the screen.
            window3Obj.addstr(window3[3] - 2, 0, window3Caption,
                              curses.color_pair(3) | curses.A_BOLD)
        window3Obj.refresh()

        # Necessary so we can "pause" on the window output before quitting.
        window3Obj.getch()

        # Debugging output.
        # stdscr.addstr(0, 0, "Chosen layout is [" + chosenLayout + "]")
        # stdscr.addstr(1, 10, "Window 1 params are [" + str (window1)+ "]")
        # stdscr.addstr(2, 10, "Window 2 params are [" + str(window2) + "]")
        # stdscr.addstr(3, 10, "Window 3 params are [" + str(window3)+ "]")
        # stdscr.addstr(4, 10, "Colors are [" + str(colors) + "]")
        # stdscr.addstr(5, 0, "Press a key to continue.")
        # stdscr.refresh()
        # stdscr.getch()
    except Exception as err:
        caughtExceptions = str(err)

    # End of Program...
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

    # Display Errors if any happened:
    if "" != caughtExceptions:
        print("Got error(s) [" + caughtExceptions + "]")
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
