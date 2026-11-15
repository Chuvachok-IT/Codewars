def disemvowel(string_):
    wowels = "aeiouAEIOU"
    result = ""
    for i in string_:
        if i not in wowels:
            result += i
    return result
