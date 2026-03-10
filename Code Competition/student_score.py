def arrangement(student_scores):
    ascending_score = sorted(student_scores)
    descending_score = sorted(student_scores, key = lambda x:x, reverse = True)
    top_score = descending_score[:3]
    print("Arrangement of student score in ascending order: ",ascending_score)
    print("Arrangement of student score in descending order: ",descending_score)
    print("Top three student scores are: ",top_score)

student_scores = list(map(int,input("Enter the scores of student in a coding competition: ").split()))
result = arrangement(student_scores)

# Enter the scores of student in a coding competition: 54 95 49 85 76 101 7
# Arrangement of student score in ascending order:  [7, 49, 54, 76, 85, 95, 101]
# Arrangement of student score in descending order:  [101, 95, 85, 76, 54, 49, 7]
# Top three student scores are:  [101, 95, 85]
