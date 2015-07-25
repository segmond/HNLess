import requests, json, pickle, datetime

# https://github.com/HackerNews/API
class HNLess:
    def __init__(self):
        self.top_stories_ids = []
        self.stories = {}
        self.top10data = {}

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
        return self.stories
    
    def topTen(self):
        today = datetime.date.today().strftime("%m-%d-%Y")
        return sorted([(value,key) for (key,value) in self.stories.items()], reverse=True)[0:10]

    def save(self, top10):
        input = open('top10hn.pkl', 'rb')
        self.top10data = pickle.load(input)
        input.close()

        self.top10data[today] = top10

        output = open('top10hn.pkl', 'wb')
        pickle.dump(self.top10data, output)
        output.close()

    def run(self):
        self.allScores()
        top10data = self.topTen()
        self.save(top10data)

    def show(self):
        print self.top10data

app = HNLess()
app.run()
app.show()
