import re


class Solution:
    def numUniqueEmails(self, emails: list) -> int:
        # c = 0
        for j in range(len(emails)):
            # match = re.search(r'\w+@(\w+.\w)*.com', i)
            # rem = re.search(r'"+"[a-z]@', i)
            # print(match, match == i, rem)
            # if match:
            #     c += 1

            i = emails[j]
            at_the_rate = i.find('@')
            i = i[:at_the_rate].replace('.', '')+i[at_the_rate:]
            plus = i.find('+')
            at_the_rate = i.find('@')
            if plus > -1:
                i = i[:plus]+i[at_the_rate:]
            emails[j] = i

            # match = re.search(r'\w+@(\w+.\w)*.com', i)
            # if match:
            #     c += 1
        return len(set(emails))


f = Solution()
print(f.numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
print(f.numUniqueEmails(["1234tytytya@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
