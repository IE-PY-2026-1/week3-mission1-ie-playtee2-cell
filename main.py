# 파일이름 : 파프입 3주차
# 작 성 자 : 60232152 김강민

# 미션 1
# 1, 사용자 입력
name2 = input("이름을 입력하시오: ")
writing2 = int(input("당신의 글쓰기 점수를 입력하시오: "))
python2 = int(input("당신의 파이썬 점수를 입력하시오: "))
last_avg2 = float(input("당신의 지난 학기 평균을 입력하시오: "))

# 2, 계산
average2 = (wrtiting2 + python2) / 2
diff = average2 - last_avg2

# 3, 출력
print("")
print(f"{name2} 학생의 글쓰기 점수는 {writing2}, 파이썬 점수는 {python2} 입니다.")
print(f"평균은 {average2}이고, 지난 학기와의 차이는 {diff} 입니다.")
