import json # allows storage of data in json file format

Jobs = [] #  Creates a list (storage)

def load_jobs(): # defines function that loads job data from json file 
    global Jobs # makes sure we are dealing with the jobs list defined at the beginning of the program. additionally, lines 5-20 handles errors 
    try:
        with open("jobs.json","r") as file:
            Jobs = json.load(file)
    except FileNotFoundError:
        Jobs = [] # if file not found, initializes empty list
    except json.JsondecodeError:
        Jobs = [] # if json is invalid, initializes empty list

def save_jobs(): # defines function that saves jobs to json
    with open ("jobs.json","w") as file:
        json.dump(Jobs,file,indent=4) # saves the Jobs list to a file named "jobs.json" in JSON format, with an indentation of 4 spaces for better readability.

load_jobs() # Load existing jobs when the program starts

while True: # This creates a loop
    print("All Year Roofing and Construction") # lines 3-8 express a user interface
    print("Brito Systems: ContractorOS v0.2")
    print("Early Development Software")
    print("Software Engineer: Austin Brito")
    print(" Hello Mark, welcome to your job checker. You can add a job, show total profit, clear all jobs, find a job by name, edit a job, or exit the program. " \
    "")
    command = input("Type 'add', 'show', 'clear', 'find', 'edit', or 'exit': ").strip().lower() # this line adds the interactive element to the program, allowing the user to input commands and interact with the job checker system. The input is processed to ensure it is in a consistent format (lowercase and stripped of extra whitespace) for easier command handling.
    
    if command == 'add': # if the user types 'add', the program will execute the following block of code to add a new job to the system.
        name = input("Enter job name: ")
        price = float(input("Enter price: "))
        location = input("Enter location: ")
        material = float(input("Enter material cost: "))
        labor = float(input("Enter labor charge: "))
        additional_fees = float(input("Enter additional fees amount: "))
        profit = labor - material - additional_fees # establishes the formula for the calculator
        Jobs.append({ # this line adds a new job to the Jobs list, storing all relevant details about the job (name, location, price, material cost, labor charge, additional fees, and calculated profit) in a dictionary format for easy access and organization.
            "name": name,
            "location": location,
            "price": price,
            "material": material,
            "labor": labor,
            "additional_fees": additional_fees,
            "profit": profit
        })

        save_jobs() # this line calls the save_jobs() function to save the updated list of jobs to the "jobs.json" file, ensuring that the new job is stored persistently for future access.
        print("Job added successfully.")

        total_profit = sum(job["profit"] for job in Jobs)
        if price > 5000: # lines 28-43 evaluate the price and profit of the job and categorize it accordingly, providing feedback to the user about the value and efficiency of the job based on predefined thresholds.
            print(name, "High Value Job")
        elif price > 2200:
            print(name, "Valuable job")
        else:
            print(name, "mediocre job")
        if profit > 5000:
            print(name, "High Efficiency Job")
            print("Profit:", profit)
        elif profit > 2200:
            print(name, "Medium Efficiency Job")
        else:
            print(name, "Low Efficiency Job")
        print("Profit:", profit)
        print("Total profit:", total_profit)
    elif command == 'show': # if the command isnt 'add' checks if command is 'show' if the user types 'show', the program will calculate and display the total profit from all jobs currently stored in the system.
        total_profit = sum(job["profit"] for job in Jobs)
        print("Current Total Profit:", total_profit)
    elif command == 'clear': # if the command isnt 'add' or 'show', checks if command is 'clear' if the user types 'clear', the program will remove all jobs from the system, effectively resetting the job list and clearing any stored data about previous jobs.
         Jobs.clear()
         save_jobs() # this line calls the save_jobs() function to save the now-empty list of jobs to the "jobs.json" file, ensuring that all previous job data is removed from persistent storage as well.
         print("All jobs erased")
    elif command =='find': # if the command isnt 'add', 'show', or 'clear' checks if command is 'find' if the user types 'find', the program will prompt the user to enter a job name and then search through the list of jobs to find any that match the provided name. If a matching job is found, its details (name, location, price, material cost, labor charge, additional fees, and profit) will be displayed. If no matching job is found, a message indicating that the job was not found will be printed.
        search_name = input("Enter job name to find: ") 
        found_jobs = [job for job in Jobs if job["name"] == search_name] # this line uses a list comprehension to search through the Jobs list and create a new list (found_jobs) that contains all jobs whose "name" field matches the search_name provided by the user. This allows for efficient searching and retrieval of job details based on the job name.
        if found_jobs:
            for job in found_jobs:
                print("Name:", job["name"])
                print("Location:", job["location"])
                print("Price:", job["price"])
                print("Material Cost:", job["material"])
                print("Labor Charge:", job["labor"])
                print("Additional Fees:", job["additional_fees"])
                print("Profit:", job["profit"])
                break
        else:
            print("Job not found.")
    elif command == 'edit': # if the command isnt 'add', 'show', 'clear', or 'find' checks if command is 'edit' if the user types 'edit', the program will prompt the user to enter a job name and then search through the list of jobs to find any that match the provided name. If a matching job is found, the program will allow the user to edit the details of that job (name, location, price, material cost, labor charge, additional fees) and then recalculate the profit based on the updated information. If no matching job is found, a message indicating that the job was not found will be printed.
        search_name = input("Enter job name to edit: ")

        found_jobs = None
        for job in Jobs:
            if job["name"] == search_name:
                found_jobs = job
                break  
        if found_jobs:
            print("Job found. Leave blank to keep current value.")

            new_name = input(f"Enter new name for {found_jobs['name']}: ").strip()
            if new_name:
                found_jobs["name"] = new_name
            new_location = input(f"Enter new location for {found_jobs['name']}: ").strip()
            if new_location:
                found_jobs["location"] = new_location
            new_price = input(f"Enter new price for {found_jobs['name']}: ").strip()
            if new_price:
                found_jobs["price"] = float(new_price)
            new_material = input(f"Enter new material cost for {found_jobs['name']}: ").strip()
            if new_material:
                found_jobs["material"] = float(new_material)
            new_labor = input(f"Enter new labor charge for {found_jobs['name']}: ").strip()
            if new_labor:
                found_jobs["labor"] = float(new_labor)
            new_additional_fees = input(f"Enter new additional fees for {found_jobs['name']}: ").strip()
            if new_additional_fees:
                found_jobs["additional_fees"] = float(new_additional_fees)
                found_jobs["profit"] = (
                    found_jobs["price"]
                    - found_jobs["material"]
                    - found_jobs["labor"]
                    - found_jobs["additional_fees"]
                )

                save_jobs()
                print("Job updated successfully.")

        else:print("job not found.")

    elif command == 'exit': # if the command isnt 'add', 'show', 'clear', or 'find' checks if command is 'exit' if the user types 'exit', the program will calculate and display the total profit from all jobs currently stored in the system, evaluate whether the overall business is profitable based on a predefined threshold, and then terminate the program with a goodbye message.
        print("Goodbye")
        break
    else: # if the command does not match any of the predefined commands ('add', 'show', 'clear', 'find', or 'exit'), the program will execute this block of code, which simply prints an error message indicating that the command is invalid and prompts the user to try again.
        print("Invalid command. Please try again.")
total_profit = sum(job["profit"] for job in Jobs)
print("Total profit:", total_profit)
if total_profit > 18867.924528:
    print("Overall, the business is profitable")
    # WORK IN PROGRESS SYSTEM
    # 4/14/2026
    # FUTURE PRIORITIES: SMART MEMORY, AUTOMATED ANALYTICS, CLOUD INTEGRATION, USER INTERFACE ENHANCEMENTS, SECURITY IMPROVEMENTS, PERFORMANCE OPTIMIZATION, SCALABILITY SOLUTIONS, AI-DRIVEN INSIGHTS, REAL-TIME MONITORING, CUSTOMIZATION OPTIONS