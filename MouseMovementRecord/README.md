Recording mousemovement with PyAutoGUi

# This should be run at Command Prompt. Don't run In IDLE. You won't get correct output.

## At a high level, here’s what your program should do:

1) Display the current x- and y-coordinates of the mouse cursor.

2) Update these coordinates as the mouse moves around the screen.

## This means your code will need to do the following:

1) Call the position() function to fetch the current coordinates.

2) Erase the previously printed coordinates by printing \b backspace characters to the screen.

3) Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit.
