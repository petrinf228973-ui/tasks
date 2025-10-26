#include <iostream>
#include <vector>
using namespace std;

int interpolationSearch(vector<int>& arr, int x) {
    int low = 0, high = arr.size() - 1;

    while (low <= high && x >= arr[low] && x <= arr[high]) {
        if (low == high) {
            if (arr[low] == x) return low;
            return -1;
        }

        int pos = low + ((x - arr[low]) * (high - low)) / (arr[high] - arr[low]);

        if (arr[pos] == x)
            return pos;
        if (arr[pos] < x)
            low = pos + 1;
        else
            high = pos - 1;
    }
    return -1;
}

int main() {
    vector<int> arr = {10, 20, 30, 40, 50, 60, 70};
    int x = 50;

    cout << "Массив: ";
    for (int n : arr) cout << n << " ";
    cout << endl;

    int result = interpolationSearch(arr, x);
    if (result != -1)
        cout << "Элемент " << x << " найден на позиции " << result << endl;
    else
        cout << "Элемент " << x << " не найден" << endl;

    return 0;
}
