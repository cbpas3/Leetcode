def romanToInt(s: str) -> int:
    converter = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    separated = list(s)
    sum = 0
    for currentIndex in range(len(separated)):
        if currentIndex != len(separated)-1:
            if converter[separated[currentIndex]] >= converter[separated[currentIndex + 1]]:
                sum += converter[separated[currentIndex]]
            else:
                sum -= converter[separated[currentIndex]]
        else:
            sum += converter[separated[currentIndex]]
    return sum

print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))