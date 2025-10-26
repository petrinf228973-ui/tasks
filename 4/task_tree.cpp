#include <iostream>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
    Node(int k) { key = k; left = right = nullptr; }
};

Node* insert(Node* root, int key) {
    if (!root) return new Node(key);
    if (key < root->key) root->left = insert(root->left, key);
    else if (key > root->key) root->right = insert(root->right, key);
    return root;
}

Node* minValue(Node* node) {
    Node* cur = node;
    while (cur && cur->left) cur = cur->left;
    return cur;
}

Node* del(Node* root, int key) {
    if (!root) return root;
    if (key < root->key) root->left = del(root->left, key);
    else if (key > root->key) root->right = del(root->right, key);
    else {
        if (!root->left) return root->right;
        else if (!root->right) return root->left;
        Node* temp = minValue(root->right);
        root->key = temp->key;
        root->right = del(root->right, temp->key);
    }
    return root;
}

void inorder(Node* root) {
    if (root) {
        inorder(root->left);
        cout << root->key << " ";
        inorder(root->right);
    }
}

Node* search(Node* root, int key) {
    if (!root || root->key == key) return root;
    if (key < root->key) return search(root->left, key);
    else return search(root->right, key);
}

int main() {
    Node* root = nullptr;
    int a[] = {8,3,10,1,6,14,4,7,13};
    for (int x : a) root = insert(root, x);
    cout << "Обход: ";
    inorder(root);
    cout << endl;
    root = del(root, 3);
    cout << "После удаления 3: ";
    inorder(root);
    cout << endl;
    int f = 7;
    cout << "Поиск " << f << ": " << (search(root, f) ? "найден" : "нет") << endl;
}
