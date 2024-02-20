import collections
class Solution:
    def closestKValues(self, root, target, k):
        dq = collections.deque()

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            dq.append(root.val)
            inorder(root.right)

    
        inorder(root)

       
        while len(dq) > k:
            if abs(dq[0] - target) > abs(dq[-1] - target):
                dq.popleft()
            else:
                dq.pop()

        return list(dq)


if __name__ == "__main__":
  
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

   
    sol = Solution()
    target = 3.8
    k = 2
    result = sol.closestKValues(root, target, k)
    print("Closest K values to", target, "are:", result)