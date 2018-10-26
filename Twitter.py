import collections
import itertools
import heapq


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet = collections.defaultdict(collections.deque)
        self.followee = collections.defaultdict(set)
        self.count = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if len(self.tweet[userId]) > 10:
            self.tweet[userId].pop()
        self.tweet[userId].appendleft((tweetId, self.count))
        self.count += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        l = list(itertools.chain(*(self.tweet[u] for u in self.followee[userId] | {userId})))
        snews = sorted(l, key=lambda tup: tup[1], reverse=True)
        # for u in self.followee[userId] | {userId}:
        #     news += self.tweet[u]
        # snews = sorted(list(news)[:100], key=lambda tup: tup[1], reverse=True)
        # snews = list(collections.OrderedDict.fromkeys(snews))
        return list(map(lambda tup: tup[0], snews))

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followee[followerId].discard(followeeId)


def gettup(tup):
    return tup[0]


# twitter = Twitter()
# twitter.postTweet(2, 5)
# twitter.postTweet(2, 8)
# twitter.follow(1, 2)
# twitter.follow(1, 2)
# print(twitter.getNewsFeed(1))

# twitter.unfollow(1, 2)

# twitter.getNewsFeed(1);

a = collections.deque()
a.appendleft([200, 10])
a.appendleft([2, 3])
a.appendleft([2])
a.appendleft([1])
print(a)
l = list(itertools.chain(*(t for t in a)))
print("--", l)
r = heapq.merge(*(t for t in a))
print([n for n in itertools.islice(r, 10)])
