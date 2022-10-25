#If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 
# 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.



def count(n):
    letter_count = 0
    num_1_19 = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
    num_10s = {2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
    num_100s = {1:10,2:10,3:12,4:11,5:11,6:10,7:12,8:12,9:11,10:11}

    for a in range(1,n+1):
        num_list = [int(x) for x in str(a)]
        
        if len(num_list) == 1:
            letter_count += num_1_19[a]
        
        if len(num_list) == 2 and num_list[1] == 0 and num_list[0] !=1:
            letter_count += num_10s[num_list[0]]
        elif len(num_list) == 2 and num_list[0] == 1:
            letter_count += num_1_19[a]
        elif len(num_list) == 2 and num_list[0] >1 and num_list[1] != 0:
            letter_count += num_10s[num_list[0]]
            letter_count += num_1_19[num_list[1]]
        
        if len(num_list) == 3 and num_list[1] == 0 and num_list[2] == 0:
            letter_count += num_100s[num_list[0]]
        elif len(num_list) == 3 and num_list[1] == 0 and num_list[2] != 0:
            letter_count += num_100s[num_list[0]] 
            letter_count += 3
            letter_count += num_1_19[num_list[2]]
        elif len(num_list) == 3 and num_list[1] == 1:
            letter_count += num_100s[num_list[0]] 
            letter_count += 3
            k = int(str(num_list[1])+str(num_list[2]))
            letter_count += num_1_19[k]
        elif len(num_list) == 3 and num_list[2] == 0:
            letter_count += num_100s[num_list[0]] 
            letter_count += 3
            letter_count += num_10s[num_list[1]]
        elif len(num_list) == 3 :
            letter_count += num_100s[num_list[0]] 
            letter_count += 3
            letter_count += num_10s[num_list[1]]
            letter_count += num_1_19[num_list[2]]
        if len(num_list) == 4:
            letter_count += 11
        
        

    return letter_count

print(count(1000))



