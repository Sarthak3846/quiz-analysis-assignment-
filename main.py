import json
import pandas as pd
import matplotlib.pyplot as plt

current_quiz_path = "C:\\Users\\Sarthak Tyagi\\Downloads\\rJvd7g.json"
historical_quiz_path = "C:\\Users\\Sarthak Tyagi\\Downloads\\XgAgFJ.json"
quiz_details_path = "C:\\Users\\Sarthak Tyagi\\Downloads\\LLQT.json"

with open(current_quiz_path, 'r') as f:
    current_quiz_data = json.load(f)
with open(historical_quiz_path, 'r') as f:
    historical_quiz_data = json.load(f)
with open(quiz_details_path, 'r') as f:
    quiz_details = json.load(f)

def analyze_performance(historical_data):
    topics = {}

    for entry in historical_data:
        topic = entry['quiz']['topic']
        accuracy = float(entry['accuracy'].strip('%'))
        correct_answers = entry['correct_answers']
        incorrect_answers = entry['incorrect_answers']

        if topic not in topics:
            topics[topic] = {'correct': 0, 'incorrect': 0, 'accuracy': []}

        topics[topic]['correct'] += correct_answers
        topics[topic]['incorrect'] += incorrect_answers
        topics[topic]['accuracy'].append(accuracy)

    for topic in topics:
        topics[topic]['average_accuracy'] = sum(topics[topic]['accuracy']) / len(topics[topic]['accuracy'])

    return topics

def generate_recommendations(performance):
    recommendations = []

    for topic, data in performance.items():
        if data['average_accuracy'] < 70:
            recommendations.append(f"Your accuracy in '{topic}' is below 70%. Focus on practicing more questions in this area.")
        elif data['incorrect'] > 5:
            recommendations.append(f"You've made several mistakes in '{topic}'. Spend some time reviewing this topic.")

    return recommendations

def visualize_performance(performance):
    topics = list(performance.keys())
    accuracies = [performance[topic]['average_accuracy'] for topic in topics]
    plt.figure(figsize=(10, 6))
    plt.bar(topics, accuracies, color='skyblue')
    plt.xlabel('Topics')
    plt.ylabel('Average Accuracy (%)')
    plt.title('Your Topic-wise Performance')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    print("\nAnalyzing your performance...")

    # Analyze performance
    performance = analyze_performance(historical_quiz_data)

    # Generate and display recommendations
    print("\nPersonalized Recommendations:")
    recommendations = generate_recommendations(performance)
    for rec in recommendations:
        print(f"- {rec}")

    # Visualize performance
    print("\nGenerating your performance chart...")
    visualize_performance(performance)
