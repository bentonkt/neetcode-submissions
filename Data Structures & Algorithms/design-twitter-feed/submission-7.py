import heapq 

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follows[userId].add(userId)
        self.posts[userId].append((self.time, tweetId))

        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follows[userId]
        res = []
        heap = []

        for u in users: 
            if self.posts[u]:
                heapq.heappush(heap, (self.posts[u][-1], len(self.posts[u])-1, u))
        i = 0
        while heap and i < 10: 
            (time, x), index, u = heapq.heappop(heap)
            res.append(x)
            if index - 1 >= 0:
                heapq.heappush(heap, (self.posts[u][index-1], index-1, u))
            i+=1

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
