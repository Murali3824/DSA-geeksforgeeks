class Solution:
    def InfixtoPostfix(self, s):
        def priority(op):
            if op == '+' or op == '-':
                return 1
            elif op == '*' or op == '/':
                return 2
            elif op == '^':
                return 3
            else:
                return 0

        ans = ""
        st = []
        i = 0
        n = len(s)

        while i < n:
            if s[i].isalnum():  # Operand (A-Z, a-z, 0-9)
                ans += s[i]
            elif s[i] == '(':
                st.append(s[i])
            elif s[i] == ')':
                while st and st[-1] != '(':
                    ans += st.pop()
                if st and st[-1] == '(':
                    st.pop()
            else:
                while st and priority(s[i]) <= priority(st[-1]):
                    ans += st.pop()
                st.append(s[i])
            i += 1

        while st:
            ans += st.pop()

        return ans
