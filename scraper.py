import praw
import sys


def getReddit(sub, sort, time_filter, limit):
	if sort == 'new':
		sub = reddit.subreddit(sub).new(time_filter=time_filter, limit=limit)
	elif sort == 'top':
		sub = reddit.subreddit(sub).top(time_filter=time_filter, limit=limit)
	elif self.sort == 'hot':
		sub = reddit.subreddit(sub).hot(time_filter=time_filter, limit=limit)
	else:
		sub = reddit.subreddit(sub).hot(time_filter=time_filter, limit=limit)

	post = {}
	for p in sub:
		post['selftext'] = p.selftext
		post['title'] = p.title
		post['id'] = p.id

	print(post)

	return post

def getComments(post, sort, limit):
	submission = reddit.submission(id=post['id'])
	submission.comment_sort = sort
	submission.comment_limit = limit

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

	post = getReddit(sub=sys.argv[6], sort='top', time_filter='week', limit=1) # get top post of sub reddit
	comments = getComments(post=post, sort='best', limit=10) # get top comments, well try atleast
	for k, v in comments.items():
		print(k)
		print(v)
		print('---------------------------------')


