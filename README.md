#  Task 2: Data Visualization & Storytelling — Netflix Dataset
**Tool: Tableau Public (Free) | Dataset: Netflix Movies & TV Shows**

##  Objective
Create compelling visualizations that tell a business story using the Netflix dataset in Tableau Public — demonstrating chart selection, color theory, filters, and data storytelling.

##  Tools Used
- **Tableau Public** (free at https://public.tableau.com)
- **Dataset:** Netflix Movies & TV Shows — 8,807 titles, 8 columns

##  Project Structure
```
task2-netflix-tableau/
├── netflix_titles.csv            ← Upload this to Tableau
├── generate_dataset.py           ← Script that created the dataset
├── tableau_guide.md              ← Step-by-step Tableau instructions
├── screenshots/
│   ├── 01_content_type_donut.png
│   ├── 02_content_per_year.png
│   ├── 03_top_countries.png
│   ├── 04_top_genres.png
│   ├── 05_ratings.png
│   ├── 06_release_trend.png
│   └── 07_dashboard.png
└── README.md
```

##  Visualizations Built in Tableau

| # | Chart Type | Fields Used | Business Insight |
|---|-----------|-------------|-----------------|
| 1 | Donut Chart | Type | 69.6% Movies vs 30.4% TV Shows |
| 2 | Grouped Bar + Line | date_added_year, Type | Peak content growth in 2017–2019 |
| 3 | Horizontal Bar | Country | USA leads (35%), India is #2 |
| 4 | Bar Chart | listed_in (Genre) | Dramas dominate all genres |
| 5 | Bar Chart | Rating | TV-MA = 36% — adult-focused platform |
| 6 | Area Chart | release_year, Type | Content concentrated post-2015 |
| 7 | Dashboard | All fields | Full KPI + multi-chart view |

##  How to Build in Tableau Public
1. Download Tableau Public free from https://public.tableau.com/en-us/s/download
2. Open Tableau → Connect → Text File → select `netflix_titles.csv`
3. Go to Sheet 1 — drag fields to Rows/Columns/Color/Size
4. Follow the step-by-step guide in `tableau_guide.md`
5. Build a Dashboard → drag all sheets onto the canvas
6. Publish to Tableau Public → copy the public link for GitHub README

##  Key Business Insights
1. Netflix has 2.3x more Movies than TV Shows — TV Shows drive longer engagement (opportunity)
2. Content additions peaked in 2019, slowing post-COVID — budget tightening signal
3. USA produces 35% of content; India is #2 driven by Bollywood demand
4. Dramas dominate; International content is the fastest-growing category
5. TV-MA (adult) = 36% — Netflix is primarily an adult entertainment platform
6. Most content was released after 2015 — platform focuses on fresh, modern titles

