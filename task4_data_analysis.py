# Analyse student scores

scores = {
    "John": 75,
    "Mary": 82,
    "David": 68,
    "Sarah": 90,
    "Peter": 85
}

highest = max(scores.values())
lowest = min(scores.values())
average = sum(scores.values()) / len(scores)

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)