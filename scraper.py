import praw
import sys


class SubredditScraper:
	def __init__(self, sub, sort='new', time='all', lim=100):
		self.sub = sub
		self.sort = sort
		self.time = time
		self.lim = lim


	def set_sort(self):
		if self.sort == 'new':
			return self.sort, reddit.subreddit(self.sub).new(time_filter=self.time, limit=self.lim)
		elif self.sort == 'top':
			return self.sort, reddit.subreddit(self.sub).top(time_filter=self.time, limit=self.lim)
		elif self.sort == 'hot':
			return self.sort, reddit.subreddit(self.sub).hot(time_filter=self.time, limit=self.lim)
		else:
			self.sort = 'hot'
			return self.sort, reddit.subreddit(self.sub).hot(time_filter=self.time, limit=self.lim)

	def get_posts(self):
		post = {}
		sort, subreddit = self.set_sort()

		for p in subreddit:
			post['selftext'] = p.selftext
			post['title'] = p.title
			post['id'] = p.id

		print(post)

		return post


	def get_comments(self, post):
		submission = reddit.submission(id=post['id'])
		submission.comment_sort = 'best'
		submission.comment_limit = 3
		res = {}

		for comment in submission.comments:
			try:
				res[comment.author] = comment.body
			except:
				pass


		return res

if __name__ == "__main__":
	reddit = praw.Reddit(client_id = sys.argv[1],
					client_secret = sys.argv[2],
					username = sys.argv[3],
					password = sys.argv[4],
					user_agent = sys.argv[5])

	data = SubredditScraper(sys.argv[6], sort='top', time='week', lim=1)
	post = data.get_posts()
	important = data.get_comments(post)
	for k, v in important.items():
		print(k)
		print(v)
		print('---------------------------------')