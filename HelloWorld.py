
# Initialize the variables to be used
svIP = ''
ivSegCnt = 0
ivCharCnt = 0
ivCharIndex = 0

# Get input from the user
svIP = input('Enter the IP address ')

# Double-check for starting '.' character
# Note - this only checks for ONE wrong starting
# character... there is a lot more validation checking
# that can be done.
if svIP[0] == '.':  # check opening char for '.'
    ivCharIndex = 1 # if it is - then don't look at it
    if svIP[1] == '.':  # if the second char is also a '.'
        print()
                        # we have a big problem
        print('Houston - we have a problem...')
        exit(1) # exit the program

# Start cycling through the input
for i in range(ivCharIndex, len(svIP)):
    if svIP[i] == '.':  # if the character is a '.'
        ivSegCnt += 1   # increment the seg count
        # print out the segment stats
        print('Segment {} has {} chars'.format(ivSegCnt, ivCharCnt))
        ivCharCnt = 0   # zero the character count
    else:               # if the char was NOT a '.'
        ivCharCnt += 1  # increment the char count

    if i == (len(svIP)-1):  # check the last character

        if svIP[i] == '.':  # don't be fooled by an ending '.'
            continue        # end this loop
        else:
            ivSegCnt += 1   # if not a trailing '.' then increment the seg count
            print('Segment {} has {} chars'.format(ivSegCnt, ivCharCnt))

print('Total number of segments is {}'.format(ivSegCnt))
