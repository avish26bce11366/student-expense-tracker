import user_profile
import expense_log
import reports

def show_dashboard_options():
    print("\n***********************************")
    print("   CAMPUS POCKET MONEY TRACKER     ")
    print("***********************************")
    print("1. Set Up My Student Profile & Limit")
    print("2. Show My Profile Details")
    print("3. Enter a New Bill/Expense")
    print("4. See All Logged Bills")
    print("5. Generate Budget Alert Summary")
    print("6. Save Data & Exit Program")
    print("***********************************")

def start_app():
    while True:
        show_dashboard_options()
        user_pick = input("Pick an option (1-6): ").strip()
        
        if user_pick == "1":
            user_profile.configure_user()
        elif user_pick == "2":
            user_profile.display_user()
        elif user_pick == "3":
            expense_log.log_new_spend()
        elif user_pick == "4":
            expense_log.show_all_spends()
        elif user_pick == "5":
            reports.print_my_summary()
        elif user_pick == "6":
            print("\nGoodbye! Stay smart with your money.")
            break
        else:
            print("\n[!] Wrong input choice. Type a number from 1 to 6.")

if __name__ == "__main__":
    start_app()

