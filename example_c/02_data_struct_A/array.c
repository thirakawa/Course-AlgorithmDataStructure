/*
 * array.c
 *
 * 配列（Array）のサンプルプログラム。
 *
 * このプログラムでは、C言語の配列を使用して、配列への要素
 * の追加と削除を行なっています。
 */

#include <stdio.h>

#define MAX_SIZE 10

// 配列への要素追加（指定位置に挿入）
void insert(int array[], int *size, int position, int value) {
    // 後ろの要素を1つずつ右へ移動
    for (int i = *size; i > position; i--) {
        array[i] = array[i - 1];
    }

    // 値を挿入
    array[position] = value;

    (*size)++;
}

// 配列から要素削除
void delete(int array[], int *size, int position) {

    // 要素を左へ詰める
    for (int i = position; i < *size - 1; i++) {
        array[i] = array[i + 1];
    }

    (*size)--;
}

// 配列の表示
void print_array(int array[], int size) {
    printf("Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

// main関数
int main() {
    // 配列の初期化
    int array[MAX_SIZE] = {10, 20, 30, 40, 50};
    int size = 5;

    // 初期配列の表示
    printf("初期配列\n");
    print_array(array, size);

    // 要素追加
    printf("\n2 番目の要素に 25 を挿入\n");
    insert(array, &size, 2, 25);
    print_array(array, size);

    // 要素削除
    printf("\n3 番目の要素を削除\n");
    delete(array, &size, 3);
    print_array(array, size);

    return 0;
}
