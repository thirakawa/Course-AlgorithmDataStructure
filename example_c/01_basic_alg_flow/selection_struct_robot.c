/*
 * selection_struct_robot.c
 *
 * 選択構造（Selection structure）のサンプルプログラム。
 *
 * 条件分岐を含む演算例を示しています。
 * 
 * このスクリプトでは講義「03-アルゴリズムを表現する方法」で解説した
 * 「ロボットのおつかい」で紹介した選択構造のプログラムを実行します。
 */

#include <stdio.h>

int main(void) {
    printf("プログラム開始\n");

    printf("スーパーに着きました。\n");
    printf("しらたきを買おうと思います。\n");

    // スーパーにしらたきがあるかを [y/n] で入力
    char a;
    printf("スーパーにしらたきはありますか？ [y/n]: ");
    scanf("%c", &a);

    // 入力した結果によって異なる動作を実行
    if (a == 'y') {
        printf("しらたきがあるので、しらたきを買いました。\n");
    } else if (a == 'n') {
        printf("しらたきが無かったので、代わりに糸こんにゃくを買いました。\n");
    } else {
        printf("しらたきがあるかどうかわかりませんでした。\n");
        printf("y (yes) または n (no) で答えてください。\n");
    }

    printf("家に帰ります。\n");

    printf("プログラム終了\n");

    return 0;
}
