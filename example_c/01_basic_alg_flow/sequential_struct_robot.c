/*
 * sequential_struct_robot.c
 *
 * 順次構造（Sequential structure）のサンプルプログラム。
 *
 * 上から下へ一連の処理を順番に実行し、分岐や繰り返しを含まない
 * 単純な演算例を示しています。
 * 
 * このスクリプトでは講義「03-アルゴリズムを表現する方法」で解説した
 * 「ロボットのおつかい」で紹介した順次構造のプログラムを実行します。
 */

#include <stdio.h>

int main(void) {
    printf("プログラム開始\n");

    printf("スーパーマーケットに行きます。\n");

    printf("しらたきを買います。\n");

    printf("家に帰ります。\n");

    printf("プログラム終了\n");

    return 0;
}
