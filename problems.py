import re


def problem1(searchstring):
    """
    Match emails.

    :param searchstring: string
    :return: True or False
    """
    match = re.compile(r'^(?!0)([1-7]\d{2})\.[a-zA-Z]{1,10}(?:\d*)@(?:sheild\.gov|avengers\.com)$')
    if match.fullmatch(searchstring):
        return 'valid'
    else:
        return 'invalid'

def problem2(searchstring):
    """
    Extract hero and ship.

    :param searchstring: string
    :return: tuple
    """
    match = re.search(r'([A-Z][a-z]*(?: [A-Z][a-z]*)*) (rides|flies) (a ([A-Z][a-z]*(?: [A-Z][a-z]*)*)|([a-z]+))(?!\S)', searchstring)
    if match and match.group(4):
        hero = match.group(1)
        vehicle = match.group(4) or match.group(5)
        return (hero,vehicle)
    else:
        return('nohero', 'noname')

def problem3(searchstring):
    """
    Replace apprentice with title.

    :param searchstring: string
    :return: string
    """
    transcript = re.sub(r'(?<=[A-Z])\s+(Boy|Girl)\b', lambda match: "Man" if match.group(1).lower() == "boy" else "Woman", searchstring)
    if transcript != searchstring:
        return transcript
    else:
        return 'nomatch'

if __name__ == '__main__':
    #Added nomatch test cases for Problem 2 and 3
    print("\nProblem 1:")
    testcase11 = '123.iamironman@avengers.com'
    print("Student answer: ",problem1(testcase11),"\tAnswer correct?", problem1(testcase11) == 'valid')

    testcase12 = '250.Srogers1776@avengers.com'
    print("Student answer: ",problem1(testcase12),"\tAnswer correct?", problem1(testcase12) == 'valid')

    testcase13 = '100.nickfury@sheild.gov'
    print("Student answer: ",problem1(testcase13),"\tAnswer correct?", problem1(testcase13) == 'valid')

    testcase14 = '144.venom@avengers.comasdf'
    print("Student answer: ",problem1(testcase14),"\tAnswer correct?", problem1(testcase14) == 'invalid')

    testcase15 = '942.hyperion@avengers.com'
    print("Student answer: ",problem1(testcase15),"\tAnswer correct?", problem1(testcase15) == 'invalid')

    testcase16 = '567.greengoblin@sheild.gov'
    print("Student answer: ",problem1(testcase16),"\tAnswer correct?", problem1(testcase16) == 'invalid')

    testcase17 = '324drdoom324@avengers.com'
    print("Student answer: ",problem1(testcase17),"\tAnswer correct?", problem1(testcase17) == 'invalid')

    testcase18 = '765.Hosborn*876@sheild.gov'
    print("Student answer: ",problem1(testcase18),"\tAnswer correct?", problem1(testcase18) == 'invalid')

    testcase19 = '234.vulture@sheild.com'
    print("Student answer: ",problem1(testcase19),"\tAnswer correct?", problem1(testcase19) == 'invalid')

    print("\nProblem 2:")
    testcase21 = "Captain America rides a Harley"
    print("Student answer: ",problem2(testcase21),"\tAnswer correct?", problem2(testcase21) == ("Captain America","Harley"))

    testcase22 = "No one rides a Harley like Ghost Rider, athough Spider Man rides a Harley with some similar expertise"
    print("Student answer: ",problem2(testcase22),"\tAnswer correct?", problem2(testcase22) == ("Spider Man", "Harley"))

    testcase23 = "Groot rides a spaceship"
    print("Student answer: ", problem2(testcase23), "\tAnswer correct?", problem2(testcase23) == ("Groot", "spaceship"))

    testcase24 = "Starlord flies a Milano"
    print("Student answer: ",problem2(testcase24),"\tAnswer correct?", problem2(testcase24) == ("Starlord", "Milano"))

    testcase25 = "The Starlord flies many ships, but Rocket flies a Warbird Special much faster"
    print("Student answer: ",problem2(testcase25),"\tAnswer correct?", problem2(testcase25) == ("Rocket", "Warbird Special"))

    testcase26 = "Spider Man flies through the city"
    print("Student answer: ",problem2(testcase26),"\tAnswer correct?", problem2(testcase26) == ("nohero", "noname"))


    print("\nProblem 3:")
    testcase31 = 'Spider Boy, I need help!'
    print("Student answer: ",problem3(testcase31),"\tAnswer correct?", problem3(testcase31) == "Spider Man, I need help!")

    testcase32 = 'There is a boy trapped in a burning building Iron Boy'
    print("Student answer: ",problem3(testcase32),"\tAnswer correct?", problem3(testcase32) == "There is a boy trapped in a burning building Iron Man")

    testcase33 = 'Spider Girl, I need help!'
    print("Student answer: ",problem3(testcase31),"\tAnswer correct?", problem3(testcase31) == "Spider Woman, I need help!")

    testcase34 = 'The Invisible girl is a member of the Fantastic Four'
    print("Student answer: ",problem3(testcase34),"\tAnswer correct?", problem3(testcase34) == "The Invisible Woman is a member of the Fantastic Four")

    testcase35 = 'There is a boy that needs to be saved from the alien!'
    print("Student answer: ",problem3(testcase35),"\tAnswer correct?", problem3(testcase35) == "nomatch")
