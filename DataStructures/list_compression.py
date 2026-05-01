nums=[1,2,3,4,5]
result=[x*2 for x in nums] 
print(result)

res= [x for x in nums if x%2==0] # filter condition
print(res)


sol=[x for x in nums if x>2 and x%2==0]
print(sol)

marks=[20,30,50,70,10]

solution=["pass" if x>=30 else "fail" for x in marks]
print(solution)


dataset=[
    {"score":90},
    {"score":80},
    {"score":100},
    {"score":70}
]

scores=[item["score"] for item in dataset]

print(scores)

text ="I Love AI" 
words=[w.lower() for w in text]
print(words)