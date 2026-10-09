import pandas as pd

def analyze_student_risk(csv_file):
    df = pd.read_csv(csv_file)
    results = []

    for index, row in df.iterrows():
        attendance = row['Attendance_Percent']
        marks = row['Internal_Marks']
        name = row['Name']
        
        # Risk Evaluation Logic
        if attendance < 60 or marks < 45:
            risk_level = "CRITICAL (Red)"
            action = "Trigger Parent Call & Remedial Classes"
        elif attendance < 75 or marks < 60:
            risk_level = "WARNING (Yellow)"
            action = "Send Warning Alert & Peer Mentoring"
        else:
            risk_level = "SAFE (Green)"
            action = "Regular Academic Monitoring"

        results.append({
            "Roll No": row['Roll_No'],
            "Name": name,
            "Attendance": f"{attendance}%",
            "Marks": f"{marks}/100",
            "Risk Level": risk_level,
            "Recommended Action": action
        })

    return pd.DataFrame(results)