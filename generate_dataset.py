import pandas as pd
import numpy as np

np.random.seed(42)
n = 8807
types = ['Movie']*6131 + ['TV Show']*2676
np.random.shuffle(types)

genres = ['Dramas','International Movies','Comedies','Action & Adventure',
          'Documentaries','Thrillers','Children & Family Movies',
          'Stand-Up Comedy','Horror Movies','Romantic Movies',
          'Crime TV Shows','Kids TV','Anime Series','Reality TV',
          'International TV Shows','Sci-Fi & Fantasy']
ratings = ['TV-MA','TV-14','TV-PG','R','PG-13','PG','NR','TV-G','G','TV-Y','TV-Y7']
rating_w = np.array([0.36,0.24,0.12,0.08,0.07,0.05,0.03,0.02,0.01,0.01,0.01])
rating_w /= rating_w.sum()
countries = ['United States','India','United Kingdom','Canada','France',
             'Japan','South Korea','Spain','Germany','Mexico',
             'Australia','Brazil','Italy','Turkey','Nigeria']
country_w = np.array([0.35,0.12,0.08,0.06,0.05,0.05,0.04,0.03,0.03,0.03,
                      0.03,0.03,0.03,0.03,0.03])
country_w /= country_w.sum()
years = list(range(2008,2022))
year_w = np.array([0.01,0.01,0.02,0.03,0.04,0.05,0.06,0.08,0.10,0.12,0.14,0.13,0.12,0.09])
year_w /= year_w.sum()

df = pd.DataFrame({
    'show_id':       [f's{i}' for i in range(1, n+1)],
    'type':          types,
    'title':         [f'Title_{i}' for i in range(1, n+1)],
    'country':       np.random.choice(countries, n, p=country_w),
    'date_added_year': np.random.choice(years, n, p=year_w),
    'release_year':  np.random.choice(years, n, p=year_w),
    'rating':        np.random.choice(ratings, n, p=rating_w),
    'listed_in':     [np.random.choice(genres) for _ in range(n)],
})
df.to_csv('/home/claude/all_tasks/task2_tableau/netflix_titles.csv', index=False)
print(f"✅ Netflix dataset saved — {n} rows, {df.shape[1]} columns")
print(df.head(3).to_string())
