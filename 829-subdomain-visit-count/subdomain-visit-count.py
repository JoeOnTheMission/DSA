class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = dict()
        out = []
        for i in range(len(cpdomains)):
            s = cpdomains[i].split(" ")
            count = int(s[0])
            link = s[1]
            d[link] = d.get(link, 0) + count

            separated_link = link.split(".")

            for j in range(1, len(separated_link)):
                sub_link = ".".join(separated_link[j:])
                d[sub_link] = d.get(sub_link, 0) + count
        for x in d:
            out.append(str(d[x]) + " " + x)
        return out 