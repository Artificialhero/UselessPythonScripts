#!python3
import sys, webbrowser, pyperclip

#Get address from clipboard or as argument
#If no address is specified, it will use the content of the clipboard.
#open webpage with Google maps to that address
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    address = pyperclip.paste()
    print(address)
    

webbrowser.open('https://www.google.com/maps/place/'+address)
