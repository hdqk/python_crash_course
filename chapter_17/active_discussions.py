import requests
from operator import itemgetter
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        # Skip over sponsored posts with zero comments.
        continue

# Sort the list by number of comments in descending order.
submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

# Process repository information.
hn_links, comments = [], []
for submission_dict in submission_dicts:
    # Turn discussion names into active links.
    title = submission_dict['title']
    hn_url = submission_dict['hn_link']
    hn_link = f"<a href='{hn_url}'>{title}</a>"
    hn_links.append(hn_link)

    comments.append(submission_dict['comments'])

# Make visualization.
title = "Most Active Discussions on HackerNews"
labels = {'x': 'Discussion', 'y': 'Comments'}
fig = px.bar(x=hn_links, y=comments, title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
