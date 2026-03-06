/*
 * linked_list.c
 *
 * リスト（List）/連結リスト（Linked list）のサンプルプログラム。
 *
 * このプログラムでは、C言語の配列を使用して、配列への要素
 * の追加と削除を行なっています。
 */

#include <stdio.h>
#include <stdlib.h>

// ノード定義
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// ノード作成
Node* create_node(int value) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = value;
    new_node->next = NULL;
    return new_node;
}

// 先頭にノード追加
Node* insert_head(Node* head, int value) {
    Node* new_node = create_node(value);

    new_node->next = head;
    head = new_node;

    return head;
}

// 指定した値の後ろにノード追加
Node* insert_after(Node* head, int target, int value) {
    Node* current = head;

    // target を探す
    while (current != NULL) {

        if (current->data == target) {

            Node* new_node = create_node(value);

            new_node->next = current->next;
            current->next = new_node;

            return head;
        }

        current = current->next;
    }

    printf("Value %d not found\n", target);
    return head;
}

// 指定値のノード削除
Node* delete_value(Node* head, int value) {
    Node* current = head;
    Node* previous = NULL;

    while (current != NULL) {

        if (current->data == value) {

            // 先頭ノードの場合
            if (previous == NULL) {
                head = current->next;
            }
            else {
                previous->next = current->next;
            }

            free(current);
            return head;
        }

        previous = current;
        current = current->next;
    }

    return head;
}

// リストの表示
void print_list(Node* head) {
    Node* current = head;
    printf("Linked List: ");
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

// main関数
int main() {
    // リストの初期化
    Node* head = NULL;
    head = insert_head(head, 30);
    head = insert_head(head, 20);
    head = insert_head(head, 10);

    // 初期リストの表示
    printf("初期リスト\n");
    print_list(head);

    // 要素を追加
    printf("\n先頭に 5 を挿入\n");
    head = insert_head(head, 5);
    print_list(head);

    // リストの途中に要素を追加
    printf("\n20 の後ろに 25 を挿入\n");
    head = insert_after(head, 20, 25);
    print_list(head);

    // 削除
    printf("\n20 を削除\n");
    head = delete_value(head, 20);
    print_list(head);

    return 0;
}