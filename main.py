# This code will convert latin characters, arabic numbers and some special characters
# to the standard morse code.
def accept():
    """Accept the string from the user"""
    text = input("Enter a text you wanted to convert to a morse text: ").upper()
    return text
def text_to_moors_code() -> dict:
    """changes the text input from the user to morse code. Returns the uppercase letters and the morse code generated"""
    user_text = accept()
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-',
                       ' ': ' / '}

    morse_char = [MORSE_CODE_DICT.get(each_char) for each_char in user_text if each_char in MORSE_CODE_DICT.keys()]
    return {
        "text" :  user_text,
        "morse_text" : " ".join(morse_char)
    }

is_continue = 'Y'
while is_continue == 'Y':
    response = text_to_moors_code()
    print(f"text: {response['text']}")
    print(f"morse-text: {response['morse_text']}")
    is_continue = input("Do you want to continue (Y/N): ").upper()

