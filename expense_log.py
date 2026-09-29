import file_io

def log_new_spend():
    all_data = file_io.read_my_file()
    if all_data["user"]["student_name"] == "":
        print("\n[!] Error: Create a profile first!")
        return

    print("\n=== LOG AN EXPENSE ===")
    item_name = input("What did you buy? (e.g. Maggie, Pen, Bus ticket): ")
    item_tag = input("Enter category (Food / Transport / Books / Fun): ")
    
    while True:
        cost_str = input("How much did it cost? Rs. ")
        if cost_str.replace('.', '', 1).isdigit(): # handles decimals simply
            item_cost = float(cost_str)
            break
        else:
            print("Invalid cost entry! Enter a clean number.")

    new_expense = {"name": item_name, "category": item_tag, "cost": item_cost}
    all_data["items_bought"].append(new_expense)
    
    file_io.write_to_file(all_data)
    print("Done! Recorded your expense.")

def show_all_spends():
    all_data = file_io.read_my_file()
    expenses_list = all_data["items_bought"]
    
    if len(expenses_list) == 0:
        print("\nYou haven't spent any money yet!")
        return

    print("\n--- Everything You Have Bought So Far ---")
    counter = 1
    for item in expenses_list:
        print(str(counter) + ".", item["name"], "[" + item["category"] + "]", "-> Rs.", item["cost"])
        counter = counter + 1
