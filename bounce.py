import time

word=str(input('Write a word! Python2 doesn\'t work for this code due to input command.'))

def bounce():
    #Importing time module so i can make words set amount of seconds
    x = 0
    
    while x != 50:
        print(word.rjust(x))
        time.sleep(0.1)
        x += 5
    if x == 50:
        while x > 5:
            print(word.rjust(x))
            time.sleep(0.1)
            x -= 5

while True:
    bounce()
