# quiz-analysis-assignment
# Setup Instructions
Ensure Python 3.7+ is installed.
Install the required Python libraries:

pip install pandas matplotlib

Download the following files and update their paths in the script:
current_quiz_path (e.g., rJvd7g.json)
historical_quiz_path (e.g., XgAgFJ.json)
quiz_details_path (e.g., LLQT.json)

Open the Jupyter Notebook or a Python environment.
Place the script (personalized_recommendations.py) in the same directory as your data files.
Run the script:

python personalized_recommendations.py

# Project Overview
# Approach
Data Analysis:
Extracted data from the provided JSON files.
Computed topic-wise accuracy, correct answers, and mistakes from historical quiz data.
# Recommendations:
Highlighted areas needing improvement (topics with <70% accuracy or frequent mistakes).
# Visualization:
Plotted a bar chart for average accuracy by topic to aid better understanding.
# Output
Text-based Insights: Summarizes strengths and weaknesses.
Visualizations: Topic-wise performance chart.
