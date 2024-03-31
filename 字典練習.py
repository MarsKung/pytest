def main_menu():
    print("\n===== 學生管理系統 =====")
    print("1. 新增學生姓名和成績")
    print("2. 刪除一個學生")
    print("3. 修改一個學生的成績")
    print("4. 顯示所有學生的姓名和成績")
    print("5. 退出")
    choice = input("請選擇一個操作 (1-5): ")
    return choice

def add_student(students):
    name = input("請輸入學生的姓名: ")
    score = input("請輸入學生的成績: ")
    #這裡應該要寫什麼?
    students[name] = score
    print(f"學生 {name} 已被新增。")

def delete_student(students):
    name = input("請輸入要刪除的學生姓名: ")
    #然後...請自己寫
    del students[name]

def modify_score(students):
    name = input("請輸入要修改成績的學生姓名: ")
    
    if name in students:
        score = input("請輸入新的成績: ")
        students[name] = score
        print(f"學生 {name} 的成績已被修改。")
  #後續請自己寫
def show_students(students):
  for name, score in students.items():
    print(f"姓名: {name}, 成績: {score}")
   #顯示所有資料，這個是能直接用的


def main():
    students = {
        "Alice": "90",
        "Bob": "85",
        "Charlie": "88",
        "David": "92",
        "Eve": "78"
    }

    while True:
        #呼叫main_menu函式，叫出選單並把輸入的選擇存到choice變數
        choice = main_menu()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            delete_student(students)
        elif choice == "3":
            modify_score(students)
        elif choice == "4":
            show_students(students)
        elif choice == "5":
            print("感謝使用學生管理系統，再見！")
            break
        else:
            print("無效的輸入，請重新輸入。")

if __name__ == "__main__":
    main()