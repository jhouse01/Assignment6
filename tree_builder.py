class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.
    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # If no root exists, insertion is impossible
        if self.root is None:
            print("⚠️ No team lead found. Add a root first.")
            return False

        # Start at the root if no node provided
        if current_node is None:
            current_node = self.root

        # If we found the manager
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to LEFT of {manager_name}.")
                    return True
                else:
                    print(f"⚠️ {manager_name} already has a LEFT report.")
                    return True

            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to RIGHT of {manager_name}.")
                    return True
                else:
                    print(f"⚠️ {manager_name} already has a RIGHT report.")
                    return True

            else:
                print("❌ Side must be 'left' or 'right'.")
                return True

        # Recursively search left subtree
        if current_node.left:
            inserted = self.insert(manager_name, employee_name, side, current_node.left)
            if inserted:
                return True  # Stop searching once inserted

        # Recursively search right subtree
        if current_node.right:
            inserted = self.insert(manager_name, employee_name, side, current_node.right)
            if inserted:
                return True

        # If we reach here and we are back at the root, manager was not found
        if current_node == self.root:
            print(f"❌ Manager '{manager_name}' not found in the team.")
        return False

    def print_tree(self, node=None, level=0):
        if self.root is None:
            print("⚠️ No team structure to display.")
            return

        if node is None:
            node = self.root

        indent = "   " * level
        print(f"{indent}- {node.name}")

        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)

'''
Implementing the team directory using a binary tree helped me understand how recursion and hierarchical data structures work together to solve real‑world organizational problems. The recursive insertion method was central in this project. Rather than manually iterate through the tree, recursion allowed the program to “walk” down each branch automatically. With each call, it handled a smaller part of the problem: check the current node and pass the baton to either a left or right child until the correct manager was found. Once the target manager was found, the function would insert the new employee and make its way back up the hierarchy, stopping any further unnecessary searching. It just made the logic so elegant and efficient.

One of the biggest challenges I faced was ensuring that I handled the situation in which the manager did not exist, and the recursion simply ended silently without doing anything. However, by introducing return values, I was able to fix this challenge and make it so that the program simply printed an error message once. Another big challenge I faced was ensuring that I did not allow duplicate insertions, which would have been a possibility because recursion would have continued exploring all the trees unless handled.

Trees find their application in real-world systems where hierarchical relationships are important, like organizational structures of companies, file systems, decision trees, and routing systems, among many more outside the realms of programming and data storage. This project attempted to show the applicability and flexibility of trees in data modeling while at the same time providing some much-needed structure in data modeling approaches.
'''
