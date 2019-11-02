#https://leetcode.com/problems/subdomain-visit-count/submissions/

from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = Counter()

        for line in cpdomains:
            count, domain = line.split()
            parent = ""
            for sub in reversed(domain.split('.')):
                cur = sub + parent
                counter[cur] += int(count)
                parent = '.' + cur

        return [f"{v} {k}" for k, v in counter.items()]
