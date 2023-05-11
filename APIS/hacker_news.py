import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS , LightenStyle as LS

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
    str(submission_id) + '.json')
    submission_r = requests.get(url)
    
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
    'title': response_dict['title'],
    'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
    'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
 reverse=True)
titles,num_comments,links=[],[],[]
for submission_dict in submission_dicts:
 print("\nTitle:", submission_dict['title'])
 print("Discussion link:", submission_dict['link'])
 print("Comments:", submission_dict['comments'])
 title=submission_dict['title']
 link=submission_dict['link']
 
 #append values to plotting lists 
 titles.append(title)
 num_comments.append(submission_dict['comments'])
 links.append(link)
 
#make a visual representation
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.show_y_guides=False
my_config.title_font_size=24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.width=1000
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_config,style=my_style)
chart.height=600
chart.title = 'Most Discussed topics in HackerNews'
chart.x_labels = titles
chart.add('',num_comments)
chart.render_to_file('Hackernews.svg')


