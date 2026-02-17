scores = list(map(int, input().split()))
avg = sum(scores) / len(scores)
if avg >= 90:
    print(avg ,"A")
elif avg >= 80:
    print(avg,"B" )
elif avg >= 70:
    print(avg,"C")
elif avg >= 60:
    print(avg, "D")
else:
    print(avg, "F")
