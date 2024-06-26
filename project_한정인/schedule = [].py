schedule =  []


number_of_subjects = int(input("몇개의 과목을 공부하고 싶나요? "))


for i in range(number_of_subjects):
    subject = input("과목의 이름을 입력하시오 " + str(i+1) + ": ")
    time = input("공부하고 싶은 시간을 입력하시오 " + subject + ": ")


    schedule.append([subject, time])


print("\n당신의 공부 스케쥴입니다:")
print("+" + "-" * 30 + "+" + "-" * 15 + "+")
print("|" + "과목".center(28) + "|" + "시간".center(13) + "|")
print("+" + "-" * 30 + "+" + "-" * 15 + "+")

for item in schedule:
    print("|" + item[0].center(28) + "|" + item[1].center(13) + "|")
    print("+" + "-" * 28 + "+" + "-" * 13 + "+")