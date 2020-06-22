import re

text_to_search = '''
abcdrfghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Needs to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

RasoulSaeidi.com

321-555-4321
123.555.1234

Mr. Saeidi
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''

Sentence = ' Start the sentence and bring it to an end'

pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
