# import pandas as pd
# import plotly.express as px

# df = pd.read_csv('data/sample.csv')
# fig = px.scatter(df, x='quantity', y='value', text='item',
#                  title='Quantity vs. Value',
#                  labels={'quantity': 'Quantity', 'value': 'Value'})

# fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
# fig.update_layout(template='plotly_white')

# # Displays
# import preswald

# preswald.text("# Welcome to Preswald!")
# preswald.text("This is your first app. 🎉")
# preswald.plotly(fig)
# preswald.table(df)

from preswald import connect, get_df, table, text, query, plotly, sidebar
import plotly.express as px
import pandas as pd


text("# My Data Analysis App")

# Load Data
connect()
df = get_df('data/student_habits_performance.csv')
df['study_hours_per_day'] = pd.to_numeric(df['study_hours_per_day'], errors='coerce')
df['exam_score'] = pd.to_numeric(df['exam_score'], errors='coerce')
table(df)

# 
# Query
sql =   """
            SELECT 
            CAST(study_hours_per_day AS DECIMAL(4,1)) AS daily_study_hours, 
            CAST(exam_score AS DECIMAL(4,1)) AS score 
            FROM data/student_habits_performance.csv 
            WHERE score > 85.0;
        """
filtered_df = query(sql, 'data/student_habits_performance.csv')

# UI
table(filtered_df)

# Visualization
fig = px.scatter(filtered_df, x='daily_study_hours', y='score',
                 title='Study Time vs. Exam Score',
                 labels={'daily_study_hours': 'study hours', 'score': 'exam scores'})
plotly(fig)
sidebar()
