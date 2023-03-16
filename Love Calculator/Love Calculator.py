# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name_1 = name1.lower()
lower_name_2 = name2.lower()

# count t
count_t_1 = lower_name_1.count("t")
count_t_2 = lower_name_2.count("t")
final_count_t = count_t_1 + count_t_2

# count r
count_r_1 = lower_name_1.count("r")
count_r_2 = lower_name_2.count("r")
final_count_r = count_r_1 + count_r_2

# count u
count_u_1 = lower_name_1.count("u")
count_u_2 = lower_name_2.count("u")
final_count_u = count_u_1 + count_u_2

# count e
count_e_1 = lower_name_1.count("e")
count_e_2 = lower_name_2.count("e")
final_count_e = count_e_1 + count_e_2

# count l
count_l_1 = lower_name_1.count("l")
count_l_2 = lower_name_2.count("l")
final_count_l = count_l_1 + count_l_2

# count o
count_o_1 = lower_name_1.count("o")
count_o_2 = lower_name_2.count("o")
final_count_o = count_o_1 + count_o_2

# count v
count_v_1 = lower_name_1.count("v")
count_v_2 = lower_name_2.count("v")
final_count_v = count_v_1 + count_v_2

# final True count
final_true_count = final_count_t + final_count_r + final_count_u + final_count_e

# final Love count
fianl_love_count = final_count_l + final_count_o + final_count_v + final_count_e

# love score
love_score = int(str(final_true_count) + str(fianl_love_count))
int_love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")