# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false


def isSameTree(self, node_1: TNode, node_2: TNode):
        # If both Trees are empty they are the same
        if node_1 == node_2 == None:
            return True
        # If node 1 is not the same as node 2 or if node 2 is not the same as node 1 
        if (not node_1 and node_2) or (node_1 and not node_2):
            return False
        # If the data is not the same return false
        if node_1.data != node_2.data:
            return False
        # Recursive statement
        return self.isSameTree(node_1.left, node_2.left) and self.isSameTree(node_1.right, node_2.right)

        #   Time complexity
        #   Because its a recursive function O(n) For how big the Trees are it only matters how big the smallest tree is.
        #   Space complexity this function creates 0 new slots in memory, it only uses memory allocated outside of function.
