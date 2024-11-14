def Options():
    print("<Your options>")
    print("1_ View tasks")
    print("2_ Add task")
    print("3_ Exit")
      
    SelectOption = input("Choose one of the options => ")
    return SelectOption
    
def View_tasks(day):
    try:
     with open(f'{day.capitalize()}file', 'r') as file:
        print(file.read())
    except FileNotFoundError:
        print(f'file {day.capitalize()} not found')
        
def Add_task(day):
        while True:
            TaskName = input("Write the topic of your task => ")
            TaskTime = input("Write your task time => ")
            
            with open(f'{day.capitalize()}File', 'a') as file:
                file.write(f"Task: {TaskName}, Time: {TaskTime}\n")
            print(f"Task added to {day.capitalize()}'s file.")
            
            more_tasks = input("Do you want to add another task? (yes/no) ").lower()
            if more_tasks != 'yes':
                break
            
def Finaly():
        while True:
            option = Options()
            if option == "1":  
                SelectDay = input("Which day's tasks do you want to see? ").lower()
                if SelectDay in ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
                    View_tasks(SelectDay)
                else:
                    print("Invalid day entered!")
            
            elif option == "2": 
                SelectDay = input("Which day's tasks do you want to add to? ").lower()
                if SelectDay in ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
                    Add_task(SelectDay)
                else:
                    print("Invalid day entered!")
            
            elif option == "3":
                print("Exiting...")
                break

            else:
                print("Invalid option selected, please try again.")


Finaly()