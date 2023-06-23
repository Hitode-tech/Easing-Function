import math

class easingfunctions:
    def easeInSine(x):
        return 1 - math.cos((x * math.pi) / 2)

    def easeOutSine(x):
        return math.sin((x * math.pi) / 2)

    def easeInOutSine(x):
        return -(math.cos(math.pi * x) - 1) / 2

    def easeInQuad(x):
        return x * x

    def easeOutQuad(x):
        return 1 - (1 - x) * (1 - x)

    def easeInOutQuad(x):
        return 2 * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 2) / 2

    def easeInCubic(x):
        return x * x * x

    def easeOutCubic(x):
        return 1 - math.pow(1 - x, 3)

    def easeInOutCubic(x):
        return 4 * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 3) / 2

    def easeInQuart(x):
        return x * x * x * x

    def easeOutQuart(x):
        return 1 - math.pow(1 - x, 4)

    def easeInOutQuart(x):
        return 8 * x * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 4) / 2

    def easeInQuint(x):
        return x * x * x * x * x

    def easeOutQuint(x):
        return 1 - math.pow(1 - x, 5)

    def easeInOutQuint(x):
        return 16 * x * x * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 5) / 2

    def easeInExpo(x):
        return 0 if x == 0 else math.pow(2, 10 * x - 10)

    def easeOutExpo(x):
        return 1 if x == 1 else 1 - math.pow(2, -10 * x)

    def easeInOutExpo(x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        elif x < 0.5:
            return math.pow(2, 20 * x - 10) / 2
        else:
            return (2 - math.pow(2, -20 * x + 10)) / 2

    def easeInCirc(x):
        return 1 - math.sqrt(1 - math.pow(x, 2))

    def easeOutCirc(x):
        return math.sqrt(1 - math.pow(x - 1, 2))

    def easeInOutCirc(x):
        return (1 - math.sqrt(1 - math.pow(2 * x, 2))) / 2 if x < 0.5 else (math.sqrt(1 - math.pow(-2 * x + 2, 2)) + 1) / 2

    def easeInBack(x):
        c1 = 1.70158
        c3 = c1 + 1
        return c3 * x * x * x - c1 * x * x

    def easeOutBack(x):
        c1 = 1.70158
        c3 = c1 + 1
        return 1 + c3 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2)

    def easeInOutBack(x):
        c1 = 1.70158
        c2 = c1 * 1.525
        return (math.pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2 if x < 0.5 else (math.pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2

    def easeInElastic(x):
        c4 = (2 * math.pi) / 3
        return 0 if x == 0 else math.pow(2, 10 * x - 10) * math.sin((x * 10 - 10.75) * c4)

    def easeOutElastic(x):
        c4 = (2 * math.pi) / 3
        return 0 if x == 0 else math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c4) + 1

    def easeInOutElastic(x):
        c5 = (2 * math.pi) / 4.5
        if x == 0:
            return 0
        elif x == 1:
            return 1
        elif x < 0.5:
            return -(math.pow(2, 20 * x - 10) * math.sin((20 * x - 11.125) * c5)) / 2
        else:
            return (math.pow(2, -20 * x + 10) * math.sin((20 * x - 11.125) * c5)) / 2 + 1

    def easeOutBounce(x):
        n1 = 7.5625
        d1 = 2.75
        if x < 1 / d1:
            return n1 * x * x
        elif x < 2 / d1:
            return n1 * (x - 1.5 / d1) * x + 0.75
        elif x < 2.5 / d1:
            return n1 * (x - 2.25 / d1) * x + 0.9375
        else:
            return n1 * (x - 2.625 / d1) * x + 0.984375

    def easeInBounce(x):
        return 1 - easingfunctions.easeOutBounce(1 - x)

    def easeInOutBounce(x):
        return (1 - easingfunctions.easeOutBounce(1 - 2 * x)) / 2 if x < 0.5 else (1 + easingfunctions.easeOutBounce(2 * x - 1)) / 2
