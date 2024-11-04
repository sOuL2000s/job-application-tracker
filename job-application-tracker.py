import pandas as pd

# Sample data for job applications
applications = {
    "Company": ["Company A", "Company B", "Company C", "Company D"],
    "Position": ["Data Analyst", "Software Engineer", "Product Manager", "Marketing Specialist"],
    "Status": ["Applied", "Interview Scheduled", "Rejected", "Awaiting Response"]
}

# Convert to DataFrame
df = pd.DataFrame(applications)

# Check for applications requiring follow-up (e.g., awaiting response)
follow_up = df[df["Status"] == "Awaiting Response"]
print("Applications requiring follow-up:")
print(follow_up)

# Show upcoming interviews
interviews = df[df["Status"] == "Interview Scheduled"]
print("\nUpcoming interviews:")
print(interviews)
