#include <iostream>
#include <vector>
using namespace std;

int binarySearch(const vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;

    while (left <= right) {
        int mid = (left + right) / 2;

        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }

    return -1;
}

int main() {
    vector<int> arr = {1, 3, 5, 7, 9, 11, 13};
    int x = 9;

    cout << "Массив: ";
    for (int n : arr) cout << n << " ";
    cout << endl;

    int result = binarySearch(arr, x);
    if (result != -1)
        cout << "Элемент " << x << " найден на позиции " << result << endl;
    else
        cout << "Элемент " << x << " не найден" << endl;

    return 0;
}
