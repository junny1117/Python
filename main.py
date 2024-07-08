import class_list
import student_list
import sys

# 등록
class_list._cls.append([])
student_list._st.append([])

Classes = class_list.Cls()
Mag = class_list.Manage()
Std = student_list.Student()
Su = student_list.Sugang()

Manager = ['hohoho', '1111']  # 관리자
class_index = 0

Classes.register(class_index, 'A12345', 2024, 1, '기초 파이썬', 3, 140, 139)
class_list._cls.append([])
class_index += 1

Classes.register(class_index, 'B12121', 2023, 2, "인공지능", 3, 75, 75)
class_list._cls.append([])
class_index += 1

Classes.register(class_index, 'B02453', 2024, 1, "딥러닝", 3, 40, 40)
class_list._cls.append([])
class_index += 1

Classes.register(class_index, 'A57431', 2024, 1, "사물 인터넷", 3, 40, 39)
class_list._cls.append([])
class_index += 1

Classes.register(class_index, 'A31245', 2023, 2, "그린 에너지 기술", 3, 40, 38)

Std.register(0, 'abcde', '1A2B3C', '240532', '홍길동', '관광경영학과', 1, ('A12345', 'B02453', 'A57431'))
student_list._st.append([])
Std.register(1, 'aaaaa', '1A2B3C', '240110', '김지원', '건축공학과', 1, ('B02453', 'A57431'))
student_list._st.append([])
Std.register(2, 'bbbbb', '1A2B3C', '222222', '김수현', '컴퓨터공학과', 1, ('A31245'))
student_list._st.append([])
Std.register(3, 'ccccc', '1A2B3C', '235555', '남궁민', '경영학과', 1, ('B12121', 'A57431'))
student_list._st.append([])
Std.register(4, 'ddddd', '1A2B3C', '211111', '박은빈', '영어영문학과', 1, ('B02453', 'A57431'))

# 로그인
def St_login():
    while True:
        input_id = input("ID를 입력하세요: ")
        input_pass = input("비밀번호를 입력하세요: ")
        if Su.search_id(input_id):
            if Su.search_pass(input_id) == input_pass:
                print("수강신청으로 들어갑니다.\n")
                break
            else:
                print("비밀번호가 다릅니다.\n")
        else:
            print("등록된 ID가 아닙니다.\n")
    
    return input_id

def Sugang_mode(input_id):
    add_sugang = []
    while True:
        code_list = list(Su.get_code(input_id))
        print("수강신청 완료 과목:", code_list)
        input_code = input("수강하려는 과목코드를 입력하세요.\n")

        if input_code in code_list:
            print("이미 수강신청한 과목입니다")
            continue
        if Mag.search_code(input_code):
            if Mag.add_subscription(input_code):
                add_sugang.append(input_code)
                add_list = code_list + add_sugang
                print(add_sugang, "과목을 추가합니다")
                add_list = tuple(add_list)
                Su.add_sugang_list(input_id, add_list)
                go = input("수강신청을 계속 하시겠습니까? Y/N: ")
                if go == "Y":
                    continue
                else:
                    code_list = list(Su.get_code(input_id))
                    print("수강신청 완료 과목입니다:")
                    print("수강신청을 종료합니다")
                    break
            else: 
                print("수강신청에 실패하였습니다.\n")
        else:
            print("해당 과목 코드가 없습니다. 다시 입력하세요")

def Mag_login():
    while True:
        man_id = input("ID를 입력하세요: ")
        man_pass = input("비밀번호를 입력하세요: ")

        if man_id == Manager[0]:
            if man_pass == Manager[1]:
                print("로그인 성공입니다")
                break
            else:
                print("비밀번호가 틀립니다\n")
        else:
            print("등록된 ID가 아닙니다.\n")

def Class_Add():
    global class_index
    while True:
        flag = input("과목을 추가할까요? Y/N:")
        if flag == "Y":
            class_list._cls.append([])
            class_index += 1
            code = input("과목코드: ")
            year = input("년도: ")
            sem = input("학기: ")
            cls = input("개설과목: ")
            cre = input("학점: ")
            tot = input("수강생수: ")
            sub = input("신청학생수: ")
            Classes.register(class_index, code, year, sem, cls, cre, tot, sub)
        
        for i in range(class_index + 1):
            print(f"{i+1}: {class_list._cls[i]}")
        print("과목 추가를 종료합니다")
        break

while True:
    mode = input("시스템 관리자는 1, 학생은 2번, 종료는 3번을 선택해주세요: ")

    if mode == "1":
        Mag_login()
        Class_Add()
    elif mode == "2":
        st_parameter = St_login()
        Sugang_mode(st_parameter)
    elif mode == "3":
        sys.exit()
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
