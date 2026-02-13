from phrase import target

def colorize(s):

    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    # print characters that match the target in green, else in red
    # only used to help with visualizing the effects of the algorithm over time
    for i in range(len(s)):
        if s[i] == target[i]:
            print(f"{GREEN}{s[i]}{RESET}", end="")
        else:
            print(f"{RED}{s[i]}{RESET}", end="")


# gen = current generation number, phr = string to print, fit = string's fitness
def summarize(gen, phr, fit):

    # cleanly summarizes the data of the "best we've seen so far"
    print(f"Generation #{gen:3}: ", end="")
    colorize(phr)
    print(f"  score: {fit:2}/{len(target)}")