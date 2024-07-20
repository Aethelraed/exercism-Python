def say(number):
    if number < 0 or number > 1000000000000 - 1:
        raise ValueError("input out of range")
    if number < 14:
        return [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
        ][number]
    if number % 1000_000_000 == 0:
        return say(number // 1000_000_000) + " billion"
    if number > 1000_000_000 - 1:
        return say(number // 1000_000_000) + " billion " + say(number % 1000_000_000)
    if number % 1000_000 == 0:
        return say(number // 1000_000) + " million"
    if number > 1000_000 - 1:
        return say(number // 1000_000) + " million " + say(number % 1000_000)
    if number % 1000 == 0:
        return say(number // 1000) + " thousand"
    if number > 1000 - 1:
        return say(number // 1000) + " thousand " + say(number % 1000)
    if number % 100 == 0:
        return say(number // 100) + " hundred"
    if number > 100 - 1:
        return say(number // 100) + " hundred " + say(number % 100)
    if number == 20:
        return "twenty"
    if number == 30:
        return "thirty"
    if number == 40:
        return "forty"
    if number == 50:
        return "fifty"
    if number < 20:
        return say(number - 10) + "teen"
    if number > 20 and number < 30:
        return say(20) + "-" + say(number - 20)
    if number > 30 and number < 40:
        return say(30) + "-" + say(number - 30)
    if number > 40 and number < 50:
        return say(40) + "-" + say(number - 40)
    if number > 50 and number < 60:
        return say(50) + "-" + say(number - 50)
    if number > 59 and number % 10 == 0:
        return str(say(number // 10) + "ty").replace("tt", "t")
    if number > 59 and number % 10 != 0:
        return say(number - number % 10) + "-" + say(number % 10)
