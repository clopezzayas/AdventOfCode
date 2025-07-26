"""
The unusual data (your puzzle input) consists of many reports, one report per line.
Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe.
The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing.
So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
"""


def get_safe_reports():
    # Result sum
    safe_reports = 0

    # Input file with historian list
    doc = open("plant-reports.txt", "r")

    for line in doc:
        report = line.split()

        previous_direction = 0  # 0 down, 1 up

        changed_direction = False
        has_invalid_distance = False

        for i in range(len(report) - 1):
            # Distance check
            first_level = int(report[i])
            second_level = int(report[i+1])
            distance = abs(first_level-second_level)

            if distance not in [1,2,3]:
                has_invalid_distance = True
                break

            # Direction check
            if first_level < second_level:
                current_direction = 1
            elif first_level > second_level:
                current_direction = 0
            else: # they are the same
                break

            # Don't check in first iteration
            if i != 0:
                if current_direction != previous_direction:
                    changed_direction = True
                    break
            previous_direction = current_direction

        if not has_invalid_distance and not changed_direction:
            safe_reports += 1

    print(f"The amount of safe reports is {safe_reports}.")
    return safe_reports

"""
    The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. 
    It's like the bad level never happened!

    Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

    More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.
    
    Thanks to the Problem Dampener, 4 reports are actually safe!

    Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""
def get_safe_reports_with_dampener():
    safe_reports = 0

    # Input file with historian list
    doc = open("plant-reports.txt", "r")


# Part 1
get_safe_reports()

# Part 2
get_safe_reports_with_dampener()