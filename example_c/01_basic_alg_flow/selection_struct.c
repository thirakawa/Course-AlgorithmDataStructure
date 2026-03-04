/*
 * selection_struct_robot.c
 *
 * 選択構造（Selection structure）のサンプルプログラム。
 *
 * 条件分岐を含む演算例を示しています。
 * 
 * このプログラムでは入力された値を比較し、必要に応じて処理の流れを分岐
 * させる構造を示します。ここでは `if` / `elif` / `else` を使い、
 * 二つの数の大小関係を判定して異なるメッセージを出力します。
 */

#include <stdio.h>

int main(void) {
    float a, b;

    // ユーザーが2つの数値を入力
    printf("一つ目の数字を入力してください: ");
    scanf("%f", &a);
    printf("二つ目の数字を入力してください: ");
    scanf("%f", &b);

    // 選択構造を使用して大小をチェック
    if (a > b) {
        printf("最初の数が大きいです。\n");
    } else if (a < b) {
        printf("二番目の数が大きいです。\n");
    } else {
        printf("両方の数は等しいです。\n");
    }

    printf("プログラム終了\n");

    return 0;
}
