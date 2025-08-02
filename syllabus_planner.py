import json

def load_curriculum(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def plan_syllabus(curriculum_data, weeks):
    # Simple example: just repeats topics over weeks
    plan = []
    topics = curriculum_data.get('weeks', [])
    for i in range(weeks):
        topic = topics[i % len(topics)]['topic']
        plan.append({'week': i+1, 'topic': topic})
    return plan

def main():
    curriculum_data = load_curriculum('datasets/sample_curriculum.json')
    weeks = 10  # number of weeks to plan
    syllabus = plan_syllabus(curriculum_data, weeks)
    print("Planned Syllabus:")
    for week_info in syllabus:
        print(f"Week {week_info['week']}: {week_info['topic']}")

if __name__ == "__main__":
    main()
