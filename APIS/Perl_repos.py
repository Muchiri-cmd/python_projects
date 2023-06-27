import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url='https://api.github.com/search/repositories?q=language:Perl&sort=stars'
r=requests.get(url)
response_dict=r.json()
print("status code: ",r.status_code)
repo_dicts=response_dict['items']

names,plot_dicts=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict={
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
    
#plot data 
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Perl Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('Perl_repos.svg')