"""	
public void printFactors(int number) {
    printFactors("", number, number);
}

public void printFactors(String expression, int dividend, int previous) {
    if(expression == "")
        System.out.println(previous + " * 1");

    for (int factor = dividend - 1; factor >= 2; --factor) {
        if (dividend % factor == 0 && factor <= previous) {
            int next = dividend / factor;
            if (nextnext <= factor)
                if (next <= previous)
                    System.out.println(expression + factor + " * " + next);

            printFactors(expression + factor + " * ", next, factor);
        }
    }
}
"""


def printFactors(num):
    print printFactorsApi("", num, num)

def printFactorsApi(s, dividend, previous):
    if dividend <= 2:
        return

    for factor in range(dividend - 1, 1, -1):
        if dividend % factor == 0:
            divisor = dividend / factor
            s += " * %s" % divisor
            printFactorsApi(s, factor )
            s += "%s" % factor
            print s

if __name__ == '__main__':
    printFactors(12)
