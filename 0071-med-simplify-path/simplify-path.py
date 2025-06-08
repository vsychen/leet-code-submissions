class Solution(object):
    # TOPICS: STRING/STACK
    # Split the path into tokens divided by slashes, ignore the empty strings. While there are tokens in the token list, check if it's ".", ".." or any other sequence of characters.
    # If it's a dot, ignore it. If it's two dots, remove one element from stack (if there's at least one). If it's anything else, add it to the stack.
    # At the end, concatenate a single slash (root slash) to a string consisting of all elements of the stack, with a single slash between each element.
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tokens = [t for t in path.split("/") if t != ""]
        stack = []
        while tokens:
            if tokens[0] == ".":
                pass
            elif tokens[0] == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(tokens[0])

            tokens.pop(0)

        return "/" + "/".join(stack)