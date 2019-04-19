#Var init
even_sum = 0
curr = 2
prev = 1
###

while curr < 4000000:
    if not (curr % 2):
        even_sum += curr
    temp = prev
    prev = curr
    curr += temp

print even_sum
