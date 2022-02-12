"""
Decode the Morse code
https://www.codewars.com/kata/54b724efac3d5402db00065e
"""


def decodeMorse(morse_code):
    morse_code = morse_code.split(" ")
    result = ""
    for l in morse_code:
        if l != '':
            result += MORSE_CODE[l]
        else:
            result += ' '
    return result.replace('  ', ' ').strip()
