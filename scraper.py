import praw
import sys
import numpy as np

def getSubreddit(sub, sort, time_filter, limit=1):
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
	post_id = post['id']
	submission = reddit.submission(id=post_id)
	submission.comment_sort = sort
	submission.comment_limit = limit

	res = {}
	for comment in submission.comments:
		try:
			res[comment.author] = comment.body
			print(f'---------------------------------------- 1 {comment.author} ----------------------------------------')
			print(comment.body)

			getRepplies(comment)
		except:
			pass

	return res

def getRepplies(comment):
	res = {}
	comment.reply_limit = 4
	for reply in comment.replies:
		res[reply.author] = reply.body
		reply.reply_limit = 2
		print(f'------------------------- 2 {reply.author} -------------------------')
		print(reply.body)
		for re in reply.replies:
			print(f'-- 3 {re.author} --')
			print(re.body)


if __name__ == "__main__":
	reddit = praw.Reddit(client_id = sys.argv[1],
		client_secret = sys.argv[2],
		username = sys.argv[3],
		password = sys.argv[4],
		user_agent = sys.argv[5])

	post = getSubreddit(sub=sys.argv[6], sort='top', time_filter='day', limit=np.random.choice(10)) # please dont make limit > 1 
	comments = getComments(post=post, sort='Best', limit=20) # get top comments, well try atleast
	