# Input Specification
# n + 1 :
# บรรทัดที่ 1 : จำนวนคำ (จำนวนเต็ม)
# บรรทัดที่ 2 ถึง n : คำ

# Output Specification
# 2 บรรทัด :
# จำนวน palindrome
# คำที่เป็น palindrome เรียงกัน
# ex. 2
# ['121', 'pip']

# 5
# Hello
# This
# Is
# TESSET
# HEPPEH

# 2
# ['TESSET', 'HEPPEH']

count = int(input())
word_list = []
for i in range(count):
    word = input()
    re_word = word [::-1]
    if word == re_word:
        word_list.append(word)
print(len(word_list))
print(word_list)
