"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet


In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

"""
# Part One - Solution
def calibration_sum():
    # Result sum
    calibration_sum = 0 
    
    # Calibration document with inputs
    doc = open("calibration-document.txt", "r")
    
    # Go through each line, filter out through numerical values in each line
    for line in doc:
        filtered = []
        for char in line:
            if char.isdigit():
                filtered.append(char)
        
    	# Grab first and last values. 
        first = filtered[0]    
        last = filtered[-1]
        
        calibration_value = str(first) + str(last)

        # parse back to int add to result sum
        calibration_sum += int(calibration_value)
    
    doc.close()
    return calibration_sum


'''
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, 
two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

'''
# Part Two - Solution
def corrected_calibration_sum():
    # Result sum
    corrected_calibration_sum = 0 
    
    # Calibration document with inputs
    doc = open("calibration-document.txt", "r")

    overlaps = {
                "oneight" : "18",
                "twone": "21",
                "threeight": "38",
                "fiveight": "58",
                "sevenine": "79",
                "eightwo": "82",
                "eighthree": "83",
                "nineight": "98"
            }
    
    # Go through each line, filter out through numerical values in each line
    for line in doc:
      
        # check for overlaps: # CRINGE AF
        for overlap in overlaps.keys():
            if overlap in line:
                new_line = line.replace(overlap, overlaps[overlap])
                line = new_line

        # Checks each string to find if they have a valid digit as substring and
        # substitutes it for proper numerical value
        index = 0
        # characters to check: o, t, f, s, e, n
        while index < len(line):
            char = line[index]
            match char:
                # case for one
                case "o":
                    if len(line)-index >= 2:     
                        substring = line[index:index+3]
                        if substring == "one":
                            new_line = line.replace("one", "1")
                            line = new_line
                # case for two/three    
                case "t":
                    if len(line)-index >= 2:     
                        substring = line[index:index+3]
                        # test for two; if not swap substring 
                        if substring == "two":
                            new_line = line.replace("two", "2")
                            line = new_line
                        
                        # test for three
                    if len(line)-index >= 4:
                        substring = line[index:index+5]
                        if substring == "three":
                            new_line = line.replace("three", "3")
                            line = new_line
                # case for four/five
                case "f":
                    if len(line)-index >= 3:     
                        substring = line[index:index+4]
                        if substring == "four":
                            new_line = line.replace("four", "4")
                            line = new_line
                        elif substring == "five":
                            new_line = line.replace("five", "5")
                            line = new_line
                # case for six/seven
                case "s":
                    if len(line)-index >= 2:     
                        substring = line[index:index+3]
                        # test for six; if not swap substring 
                        if substring == "six":
                            new_line = line.replace("six", "6")
                            line = new_line
          
                        # test for seven
                    if len(line)-index >= 4:
                        substring = line[index:index+5]
                        if substring == "seven":
                            new_line = line.replace("seven", "7")
                            line = new_line
                # case for eight
                case "e":
                    if len(line)-index >= 4:
                        substring = line[index:index+5]
                        if substring == "eight":
                            new_line = line.replace("eight", "8")
                            line = new_line
                # case for nine
                case "n":
                    if len(line)-index >= 3:
                        substring = line[index:index+4]
                        if substring == "nine":
                            new_line = line.replace("nine", "9")
                            line = new_line
            index += 1
        # same process as Solution to part 1
        filtered = []
        for char in line:
            if char.isdigit():
                filtered.append(char)

        # Grab first and last values
        first = filtered[0]    
        last = filtered[-1]
        
        calibration_value = str(first) + str(last)

        # parse back to int add to result sum
        corrected_calibration_sum += int(calibration_value)

    doc.close()
    return corrected_calibration_sum