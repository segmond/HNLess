import requests, json

# https://github.com/HackerNews/API
class HNLess:
    def __init__(self):
        self.top_stories_ids = []
        self.stories = {}

    def getTopStories(self):
        hn_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
        r = requests.get(hn_url)
        self.top_stories_ids =  r.json()

    def getItem(self, id):
        story_url = "https://hacker-news.firebaseio.com/v0/item/" + str(id) + ".json?print=pretty"
        r = requests.get(story_url)
        return  r.json()

    def getScore(self, story):
        storyJson =  json.loads(json.dumps(story))
        return storyJson['score']

    def allScores(self):
        self.getTopStories()
        for id in self.top_stories_ids:
            story = self.getItem(id)
            score = self.getScore(story)
            self.stories[id] = score
            print "story's ", id, " score is ", score
        print self.stories


app = HNLess()
app.allScores()
