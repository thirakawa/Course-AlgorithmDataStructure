/*
 * repeating_struct_robot.c
 *
 * 順次構造（Sequential structure）のサンプルプログラム。
 * 
 * 上から下へ一連の処理を順番に実行し、分岐や繰り返しを含まない
 * 単純な演算例を示しています。
 * 
 * このプログラムでは入力された正の整数（1以上の整数）をもとに、
 * 1から入力された値（`n`）までの合計とnの階乗を計算して出力します。
 */

#include <stdio.h>

int main(void) {
    int i, n;

    // 1以上の整数を入力
    printf("正の整数を入力してください: ");
    scanf("%d", &n);

    // forループを使用してnまでの合計を計算
    int total = 0;
    for (i = 0; i < n; i++) {
        total += i;
    }

    // whileループを使用して階乗を計算
    int factorial = 1;
    i = 1;
    while (i <= n) {
        factorial *= i;
        i += 1;
    }

    // 結果の表示
    printf("1 から %d までの合計: %d\n", n, total);
    printf("%d の階乗: %d\n", n, factorial);

    printf("プログラム終了\n");

    return 0;
}
