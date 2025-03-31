int test1(int x, int y) {
    while (x != y) {
        if (x > y) {
            x = x - y;
        } else {
            y = y - x;
        }
    }
    return x;
}

int test2(const std::vector<int>& arr, int search) {
    int first = 0;
    int last = arr.size();
    int middle = (last - first) / 2 + first;
    bool found = false;
    while (first <= last) {
        if (arr[middle] < search)
            first = middle + 1;
        else if (arr[middle] == search)
            found = true;
        else
            last = middle - 1;
        middle = (last - first) / 2 + first;
    }
    if (first < last) return false;
    return found;
}

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
