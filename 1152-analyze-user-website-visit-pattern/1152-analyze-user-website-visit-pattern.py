class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        hashmap = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])): 
            hashmap[user].append(site)
        
        patterns = Counter()
        for user,site in hashmap.items():
            patterns.update(Counter(set(combinations(site,3))))
            
        return max(sorted(patterns), key=patterns.get)