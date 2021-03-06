#! python3

#This is the multi clipboard project script.

import pyperclip, sys

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]   # first commandline arg is the key phrase.

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')

else:
    print(f'No text found for {keyphrase}.')

