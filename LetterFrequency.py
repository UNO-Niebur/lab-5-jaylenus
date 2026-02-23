#LetterFrequency.py
#Name: Jaylen Atsou
#Date: Feburary 22, 2026
#Assignment: Lab 5

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # loop through each character
    for ch in message:
        # Find the position in the alphabet
        spot = alpha.find(ch)

        # Increase the frequency at that position (only if it's a letter)
        if spot >= 0:
            freq[spot] = freq[spot] + 1

    # Create the output text in the format A,5\n
    output = ""
    for i in range(26):
        print(alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output = output + line

    writeToFile(output)


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)
    freqFile.close()


def main():
    msg = input("Enter a message: ")
    countLetters(msg)


if __name__ == '__main__':
    main()