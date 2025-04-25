def typing_time(layout, word):
    curr_pos = 0
    total_time = 0


    letter_positions = {}
    for index, key in enumerate(layout):
        letter_positions[key] = index
    

    for letter in word:
        # find letter position
        letter_pos = letter_positions[letter]
        # letter_pos = 0
        # for key in layout:
        #     if key == letter:
        #         break

        #     letter_pos += 1
    
        # letter_pos is the position of the next letter

        time = abs(letter_pos - curr_pos)
        total_time += time
        curr_pos = letter_pos

    return total_time



    