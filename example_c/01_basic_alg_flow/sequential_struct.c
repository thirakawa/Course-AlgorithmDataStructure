/*
 * sequential_struct.c
 *
 * 順次構造（Sequential structure）のサンプルプログラム。
 *
 * 上から下へ一連の処理を順番に実行し、分岐や繰り返しを含まない
 * 単純な演算例を示しています。
 * 
 * このスクリプトではユーザーから2つの数を受け取り、加算と減算を順に
 * 計算して結果を表示します。
 */

#include <stdio.h>

int main(void) {
    float a, b, total, diff;

    // ユーザーが2つの数値を入力
    printf("一つ目の数字を入力してください: ");
    scanf("%f", &a);
    printf("二つ目の数字を入力してください: ");
    scanf("%f", &b);

    // 足し算と割り算を一つずつ実行
    total = a + b;
    diff = a - b;

    // 結果を表示
    printf("あなたが入力した数値: %f and %f\n", a, b);
    printf("和: %f\n", total);
    printf("差: %f\n", diff);

    printf("プログラム終了\n");

    return 0;
}
