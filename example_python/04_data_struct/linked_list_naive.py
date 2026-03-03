"""linked_list_naive.py

-----------------------------------------------------------------------
リスト（List）/連結リスト（Linked list）のサンプルプログラム。

Python標準の機能を使用せずにナイーブに実装した例を
示しています。

このプログラムでは、自分で定義したNodeクラスとLinkedList
クラスを使用して、要素の追加や削除、データへのアクセスを
行なっています。
"""


# リストの要素であるノードを定義
class Node:
    def __init__(self, value):
        self.value = value  # ノードが持つ値（データ）
        self.next = None    # 次のノードを指し示す情報


# 連結リストを自分で定義
class LinkedList:
    def __init__(self):
        self.head = None  # 先頭のノード

    # リストの一番後ろにデータを追加
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # 指定した場所（インデックス）に要素を追加
    def insert(self, index, value):
        new_node = Node(value)
        
        # インデックスが0の場合は先頭に挿入
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # 挿入位置の1つ前のノードまで移動
        count = 0
        current = self.head
        
        # whileループで、要素を挿入する直前のノードまで移動
        while count < index - 1 and current is not None:
            current = current.next
            count += 1
        
        # currentがNoneの場合は無効なインデックス
        # その場合は、リストの最後に要素を追加
        if current is None:
            print(f"index: {index} が大きすぎます。")
            print(f"連結リストの最後に {value} を追加します。")
            self.append(value)
            return
        
        # 新しいノードを挿入
        new_node.next = current.next
        current.next = new_node

    # 指定した場所（インデックス）の要素を削除
    def remove(self, index):
        # 空リストの場合
        if self.head is None:
            print("リストは空です。削除できません。")
            return
        
        # 先頭を削除する場合
        if index == 0:
            self.head = self.head.next
            return
        
        # 削除対象の1つ前まで移動
        count = 0
        current = self.head
        while count < index - 1 and current is not None:
            current = current.next
            count += 1
        
        # nextがNoneならインデックスが範囲外
        if current is None or current.next is None:
            print(f"インデックス {index} は範囲外です。削除できません。")
            return
        
        # ノードをスキップして削除
        current.next = current.next.next

    # 連結リストの長さを返す
    def length(self):
        node_counter = 0
        current = self.head
        while current is not None:
            node_counter += 1
            current = current.next
        return node_counter


# ---------------------------------------------------------------------
# リストの初期化
linked_list = LinkedList()
linked_list.append("Blue")
linked_list.append("Red")
linked_list.append("Yellow")

# リストの要素の表示
count = 0
current_node = linked_list.head
while current_node is not None:
    print(f"連結リストの {count} 番目の要素:", current_node.value)
    count += 1
    current_node = current_node.next

# 今のリストの長さ（要素の数）を表示
print(f"連結リストの長さ: {linked_list.length()}")

# ---------------------------------------------------------------------
# Blue と Red の間に Green を追加
print("-" * 10)
print("Greenを0番目と1番目の間に挿入します。")

linked_list.insert(1, "Green")  # 追加

# リストの要素の表示
count = 0
current_node = linked_list.head
while current_node is not None:
    print(f"連結リストの {count} 番目の要素: {current_node.value}")
    count += 1
    current_node = current_node.next

# 今のリストの長さ（要素の数）を表示
print(f"連結リストの長さ: {linked_list.length()}")

# ---------------------------------------------------------------------
# Red （リストの 2 番目の要素）を削除
print("-" * 10)
print("リストからRedを削除します。")

linked_list.remove(2)  # 削除

# リストの要素の表示
count = 0
current_node = linked_list.head
while current_node is not None:
    print(f"連結リストの {count} 番目の要素: {current_node.value}")
    count += 1
    current_node = current_node.next

# 今のリストの長さ（要素の数）を表示
print(f"連結リストの長さ: {linked_list.length()}")
