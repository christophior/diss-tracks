# http://goo.gl/sxbh65
# Presentbot.py
import praw
import pickle
import time
import os

# Set up praw
r = praw.Reddit('disstracksserver')
CACHE_FILE = "cache"
already_done = dict()

# Load cache
# if os.path.isfile(CACHE_FILE):
#     with open(CACHE_FILE, 'r+') as file_load:
#         already_done = pickle.load(file_load)

# Caching
subreddit = r.get_subreddit('disstracks')
for post in subreddit.get_new(limit=10):
	if post.id not in already_done:
		# Do whatever you want with the post
		# Cache it
		print '\nTrack title: ' + post.title.partition(']')[-1].lstrip(' ')
		print 'Dissed Artist: ' + post.title.partition('[')[-1].rpartition(']')[0]
		print 'URL: ' + post.url
		print 'Score: ' + str(post.score)
		already_done[post.id] = post.url
	else:
		print 'Already done'

# Save cache
# with open(CACHE_FILE, 'w+') as file_save:
# 	pickle.dump(already_done, file_save)

# Get submissions from subreddit
# subreddit = r.get_subreddit('disstracks')
# submissions = subreddit.get_hot(limit=10)
# for submission in submissions:
# 	print submission.title
# 	print submission.url