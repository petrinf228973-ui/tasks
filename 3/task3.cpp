#include <iostream>
#include <vector>
#include <deque>
#include <queue>
#include <unordered_map>
using namespace std;
#include <algorithm>
int main() {
    vector<int> numbers = {5, 2, 8, 1, 3};
    cout << "Массив: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    numbers.push_back(10);
    numbers.erase(numbers.begin() + 1);
    sort(numbers.begin(), numbers.end());
    cout << "После изменений: ";
    for (int n : numbers) cout << n << " ";
    cout << endl << endl;

    vector<int> stack;
    stack.push_back(10);
    stack.push_back(20);
    stack.push_back(30);
    cout << "Стек: ";
    for (int n : stack) cout << n << " ";
    cout << endl;
    stack.pop_back();
    cout << "После pop: ";
    for (int n : stack) cout << n << " ";
    cout << endl << endl;

    deque<string> queue;
    queue.push_back("Петя");
    queue.push_back("Вася");
    queue.push_back("Маша");
    cout << "Очередь: ";
    for (auto &x : queue) cout << x << " ";
    cout << endl;
    queue.pop_front();
    cout << "После обслуживания: ";
    for (auto &x : queue) cout << x << " ";
    cout << endl << endl;

    deque<int> d;
    d.push_back(1);
    d.push_back(2);
    d.push_front(0);
    cout << "Дек: ";
    for (int x : d) cout << x << " ";
    cout << endl;
    d.pop_back();
    d.pop_front();
    cout << "После pop: ";
    for (int x : d) cout << x << " ";
    cout << endl << endl;

    priority_queue<pair<int,string>, vector<pair<int,string>>, greater<pair<int,string>>> pq;
    pq.push({2,"Вася"});
    pq.push({1,"Петя"});
    pq.push({3,"Маша"});
    cout << "Приоритетная очередь:" << endl;
    while(!pq.empty()) {
        cout << pq.top().second << endl;
        pq.pop();
    }
    cout << endl;

    struct Node {
        string data;
        Node* next;
        Node(string d) { data = d; next = nullptr; }
    };
    Node* head = new Node("Петя");
    head->next = new Node("Вася");
    head->next->next = new Node("Маша");
    cout << "Связный список: ";
    Node* temp = head;
    while(temp) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "None" << endl << endl;

    unordered_map<string, vector<int>> multi = {
        {"Петя",{5,4,3}},
        {"Маша",{4,5,5}},
        {"Вася",{3,3,4}}
    };
    for (auto &x : multi) {
        int sum = 0;
        for (int n : x.second) sum += n;
        double avg = (double)sum / x.second.size();
        cout << x.first << ": ";
        for (int n : x.second) cout << n << " ";
        cout << "средний " << avg << endl;
    }

    return 0;
}
