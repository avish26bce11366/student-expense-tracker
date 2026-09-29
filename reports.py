import file_io

def print_my_summary():
    all_data = file_io.read_my_file()
    profile = all_data["user"]
    expenses = all_data["items_bought"]

    if profile["student_name"] == "":
        print("\n[!] Setup profile first to look at financial summaries.")
        return

    total_spent = 0.0
    for e in expenses:
        total_spent = total_spent + e["cost"]

    cash_left = profile["max_limit"] - total_spent

    print("\n==================================")
    print("      MY BUDGET REPORT SUMMARY     ")
    print("==================================")
    print("Student Name      :", profile["student_name"])
    print("Total Pocket Money:", "Rs.", profile["max_limit"])
    print("Total Money Spent :", "Rs.", total_spent)
    print("Remaining Cash    :", "Rs.", cash_left)
    print("----------------------------------")

    if total_spent > profile["max_limit"]:
        print("CRITICAL WARNING: You have spent more than your total limit! Stop spending!")
    elif total_spent >= (profile["max_limit"] * 0.75):
        print("WATCH OUT: You have used up more than 75% of your cash allowances!")
    else:
        print("Safe: Your expenses are well within your limits.")

