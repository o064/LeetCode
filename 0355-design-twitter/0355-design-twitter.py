class Twitter(object):

    def __init__(self):
        self.tweets = []
        self.users ={}
        self.k = 0 

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.k -=1
        heapq.heappush(self.tweets,(self.k,[userId,tweetId]))
        if userId  not in self.users: 
            self.users[userId] = []
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users:
            return []
        ids = self.users[userId] + [userId]
        allFeeds = self.tweets[:]
        feeds = []
        while  allFeeds and len(feeds) < 10   : 
            feed = heapq.heappop(allFeeds)[1]
            feedUserId = feed[0]
            if feedUserId in ids : 
                feeds.append(feed[1])
        return feeds

        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId  not in self.users: 
            self.users[followerId] = [followeeId]
        else :
            self.users[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in  self.users  and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)