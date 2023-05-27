import pandas as pd 

south_park = pd.read_html('https://en.wikipedia.org/wiki/List_of_South_Park_episodes')
len(south_park)