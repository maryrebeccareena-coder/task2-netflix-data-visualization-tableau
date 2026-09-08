# 📋 Tableau Public — Step-by-Step Guide for Task 2

## STEP 1: Install & Connect
1. Download free at: https://public.tableau.com/en-us/s/download
2. Open Tableau Public Desktop
3. Click **Connect → Text File** → select `netflix_titles.csv`
4. Click **Sheet 1** at the bottom to start

## STEP 2: Chart 1 — Content Type Donut
1. Drag **Type** to the **Rows** shelf
2. Drag **Show_id** to **Columns** → right-click → **Measure → Count**
3. In Marks card → change chart type to **Pie**
4. Drag **Type** to **Color** in Marks card
5. Set colors: Movie = Red (#E50914), TV Show = Gold (#F5C518)
6. Right-click on pie → **Format** → make it a Donut by adding a white circle

## STEP 3: Chart 2 — Content Per Year Bar Chart
1. New Sheet → drag **date_added_year** to **Columns**
2. Drag **Number of Records** to **Rows**
3. Drag **Type** to **Color**
4. Change to **Side-by-Side Bars** in Marks
5. Title: "Content Added to Netflix Per Year"

## STEP 4: Chart 3 — Top Countries Horizontal Bar
1. New Sheet → drag **Country** to **Rows**
2. Drag **Number of Records** to **Columns**
3. Sort descending → Filter top 10
4. Change to **Horizontal Bar** chart
5. Color: dark purple gradient

## STEP 5: Chart 4 — Top Genres Bar Chart
1. New Sheet → drag **listed_in** to **Columns**
2. Drag **Number of Records** to **Rows**
3. Sort descending, filter top 10
4. Apply color by Genre

## STEP 6: Chart 5 — Ratings Distribution
1. New Sheet → drag **Rating** to **Columns**
2. Drag **Number of Records** to **Rows**
3. Sort descending
4. Color adult ratings Red, teen Yellow, kids Cyan

## STEP 7: Build the Dashboard
1. Click **New Dashboard** at the bottom
2. Drag all 5 sheets onto the canvas
3. Add Title: "Netflix Content Analysis Dashboard"
4. Add Filters: drag **Type** and **Country** → make them global filters
5. Set a consistent dark color theme

## STEP 8: Publish & Get Link
1. File → Save to Tableau Public
2. Copy the public URL
3. Add the URL to your GitHub README
