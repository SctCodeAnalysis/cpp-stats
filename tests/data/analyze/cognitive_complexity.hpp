#include <string>

int sumOfPrimes(int max) {
    int total = 0;
    for (int i = 0; i <= max; ++i) {
        int flag = 1;
        for (int j = 2; j < i; ++j) {
            if (i % j == 0) {
                flag = 0;
                break;
            }
        }
        total += i * flag;
    }
    return total;
}

int withLambda() {
    auto l = []() {
        int s = 0;
        for (int i = 0; i < 10; ++i) {
            s += i;
        }
        return s;
    };
}

void myFunc() {
    auto l = []() {
        if (true) {
            return true;
        }
    };
}
