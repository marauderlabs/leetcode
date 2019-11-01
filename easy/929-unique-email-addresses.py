# https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def purify(email: str) -> str:
            at = email.find('@')
            local = email[:at]
            local = local.replace(".", "")
            if "+" in local:
                local = local[:local.find('+')]
            return local + email[at:]

        uniq = set()
        for e in emails:
            uniq.add(purify(e))
        return len(uniq)

