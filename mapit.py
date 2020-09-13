#! python3
# USAGE: > mapit ADDRESS
# opens google maps to that address

import webbrowser, sys, pyperclip


# gets a street address from the command line arguments or clipboard
if len(sys.argv) > 1:
    # Get address from command line when running script
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

# TODO: opens web browser to the Google Maps page for the address.
# TODO: Read the command line arguments from sys.argv
# TODO: Read the clipboard contents
# TODO: Call the webbrowser.open() function to open the web browser


