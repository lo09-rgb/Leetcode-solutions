nums=[1,2,2,2,2,3,4]
count={}
for i in nums:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
f=len(nums)
for i in count:
    if count[i] > (f/2):
        print(f"majority element is{i}")

        