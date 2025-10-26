#include <iostream>
#include <vector>
using namespace std;

void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
    }
}

int main() {
    vector<int> arr = {5, 3, 8, 4, 2};
    cout << "Исходный массив: ";
    for (int x : arr) cout << x << " ";
    cout << endl;

    selectionSort(arr);

    cout << "Отсортированный массив: ";
    for (int x : arr) cout << x << " ";
    cout << endl;
    return 0;
}
