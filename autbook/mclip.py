#!/usr/bin/env python3

#mClip.py, multi clipboard program.

import sys,pyperclip

print('Welcome to the easy-reply program. What language do you wish to use?(SE/EN)')
chosenLang = str(input())

if chosenLang == 'EN':
    TEXT = {'agree':"""Yes, I agree. Sounds fine to me.""",
            'busy':"""Sorry, but I will be busy at that time. Are you able to reschedule?""",
            'hire':"""Hello! My name is Agnes, and I am very interested in working with your company.
                i am a penetration tester with much familiarity within web-development. I also enjoy python. 
                In fact, I wrote this e-mail with a python script.""" 
        }
#Add TEXT swedish version, SV_TEXT. Prompt to ask what language planned to reply in in beginning of the script.

elif chosenLang=='SE':
    TEXT={'agree':"""Ja, jag håller med! Det låter bra, tack.""",
           'busy':"""Tyvärr, jag är upptagen just då. Har du möjlighet till en annan tid?""",
            'hire':"""Hej! Mitt namn är Agnes och jag är väldigt intresserad av att jobba på erat företag.
                Jag är en penetrationstestare som har mycket vanor i webbutveckling. Jag tycker också om python.
                Det här mailet skrevs faktist med hjälp av ett python-skript jag gjort!"""
              }
    
else: 
    print('Sorry. That language does not exist.')
    sys.exit()

if len(sys.argv)<2:
    print('Usage: python3 mclip.py [agree,busy,hire] - Copies the text.')
    sys.exit()

keyphrase=sys.argv[1] #1 is the keyphrase
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' +keyphrase + ' copied to clipboard.')
    
else:
    print('There is no text for ' +keyphrase)
