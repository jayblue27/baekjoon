# 노드생성 클래스
class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

# 전위 순회 : root -> left -> right
def preorder(node):
    print(node.item, end = '')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

# 중위 순회 : left -> root -> right
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end = '')
    if node.right != '.':
        inorder(tree[node.right])

# 후위 순회 : left -> right -> root 
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end = '')


# tree 그래프 생성
N = int(input())
tree = {}
for _ in range(N):
    item, left, right = input().split()
    tree[item] = Node(item, left, right)

# 순회 - root node : A
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])