import file_io

def configure_user():
    print("\n=== SETUP NEW USER PROFILE ===")
    name_input = input("Enter your name: ")
    
    while True:
        limit_str = input("Enter your monthly budget limit (in Rupees): ")
        if limit_str.isdigit():
            money_limit = float(limit_str)
            break
        else:
            print("Please enter a valid number, don't use characters!")

    all_data = file_io.read_my_file()
    all_data["user"]["student_name"] = name_input
    all_data["user"]["max_limit"] = money_limit
    
    file_io.write_to_file(all_data)
    print("Awesome, your profile is now updated!")

def display_user():
    all_data = file_io.read_my_file()
    p = all_data["user"]
    if p["student_name"] == "":
        print("\n[!] No profile found yet! Go to option 1 first.")
    else:
        print("\n--- Current Student Info ---")
        print("Student Name:", p["student_name"])
        print("Monthly Allowance: Rs.", p["max_limit"])

