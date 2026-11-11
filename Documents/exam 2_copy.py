#these list check off "parse string data into an array" criteria
#note all this is done in the backround not output side so user cant see
#this is meant to meet the criteria of "parse string data into an array"





#original lists
def earth_items_lists():
    earth_primary_list_old = [
    "Corrupted Aphelion,not found",
    "AS-10 Bulldog,not found",
    "Blackmaw AR-47,not found",
    "Coach Gun,not found",
    "Corrupted Deceit,not found",
    "Huntmaster M1,not found",
    "Corrupted Merciless,not found",
    "Repulsor,not found",
    "Rusty Lever Action,not found",
    "Savior,not found",
    "Sporebloom,not found",
    "Starkiller,not found",
    "Widowmaker,not found",
    "Wrangler 1860,not found",
    "XMG57 Bonesaw,not found"]

    earth_secondary_list_old=[
    "Corrupted Meridian ,not found",
    "MP60-R,not found",
    "Repeater Pistol ,not found",
    "Corrupted Rune Pistol ,not found",
    "Rusty Repeater,not found",
    "Service Pistol,not found",
    "Silverback Model 500,not found",
    "Sureshot,not found",
    "Tech 22,not found",
    "Western Classic,not found"]

    
    earth_melee_list_old=[
    "Hero's Sword,not found",
    "Iron Greatsword,not found",
    "Knuckle Dusters,not found",
    "Rusted Claws,not found",
    "Scrap Hammer,not found",
    "Scrap Hatchet,not found",
    "Scrap Staff,not found",
    "Smolder,not found",
    "Steel Flail,not found",
    "Steel Spear,not found",
    "Steel Sword,not found",
    "World's Edge,not found",
    "Steel Scythe,not found",
    "Steel Katana,not found"]

    return earth_primary_list_old, earth_secondary_list_old ,earth_melee_list_old


#make a file so I can now parse in method below
def create_folder():
    earth_primary_list_old, earth_secondary_list_old ,earth_melee_list_old=earth_items_lists()

    
    with open("earth items.txt", "w") as file:
        file.write("Primary\n")
        for name in earth_primary_list_old:
            file.write(f"{name}\n")
        file.write("Secondary\n")
        for name in earth_secondary_list_old:
            file.write(f"{name}\n")
        file.write("Melee\n")
        for name in earth_melee_list_old:
            file.write(f"{name}\n")
            
#" parse string data into an array" CHECK 
def parse_folder():#concept = ["Corrupted Aphelion", "not found"]
    
    earth_primary_list = []
    earth_secondy_list = []
    earth_melee_list = []

    try: 
        with open("earth items.txt", "r") as file:
         
            current_section = None

            for line in file:
                line = line.strip()

                if line == "Primary" or line == "Secondary" or line == "Melee":
                    current_section = line  
                    continue  
            
                
                if current_section == "Primary":
                    name, status = line.split(",")
                    earth_primary_list.append([name, status])
                elif current_section == "Secondary":
                    name, status = line.split(",")
                    earth_secondy_list.append([name, status])
                elif current_section == "Melee":
                    name, status = line.split(",")
                    earth_melee_list.append([name, status])
                    
            return earth_primary_list, earth_secondy_list ,earth_melee_list

    except FileNotFoundError:
        print(" 'earth items.txt' not found")
            

        
def basic_operations(earth_primary_list, earth_secondy_list ,earth_melee_list):
    #sorting the array by alphabetic orders
    earth_primary_list.sort(key=lambda name:name[0])
    earth_secondy_list.sort(key=lambda name:name[0])
    earth_melee_list.sort(key=lambda name:name[0])

def read_file():
    try:
        with open("earth items.txt", "r") as file:
            content = file.read().strip()
            
            if not content: 
                print("Error: 'earth items.txt' is empty.")
                return False
        
    except FileNotFoundError:
        print(" 'earth items.txt' not found")
        return False
    return True
        
                
#creating the CSV file the data into a file "File must have mutiple columns" Check
def create_CSV_earth(earth_primary_list, earth_secondy_list ,earth_melee_list):
    try:
        
        with open("earth items.txt", "w") as file:
            for name,status in earth_primary_list:
                file.write(f"{name},{status},Primary,Earth\n")

            for name,status in earth_secondy_list:
                file.write(f"{name},{status},Secondary,Earth\n")
                
            for name,status in earth_melee_list:
                file.write(f"{name},{status},Melee,Earth\n")
                
    except FileNotFoundError:
        print(" 'earth items.txt' not found")

#"read a file" check
#"extracting relevant information from the file" check
# and "tranfer the processed data into a dictionary object" check

def create_earth_dictionary():
    
    earth_primary={}
    earth_secondary={}
    earth_melee={}

    try: 
    
        with open("earth items.txt", "r") as file:
            for line in file:
                name,status,category,location=line.strip().split(",") #parse each line into segments

                if category == "Primary":
                    earth_primary[name]={"Status": status, "Category": category , "Location" : location}

                elif category== "Secondary":
                    earth_secondary[name]={"Status": status, "Category": category , "Location" : location}

                elif category== "Melee":
                    earth_melee[name]={"Status": status, "Category": category , "Location" : location}

            return earth_primary , earth_secondary , earth_melee
        
    except FileNotFoundError:
        print("!!!Warning no earth items have been initiliazed!!!")
        return {}, {}, {}
    
        

#video I used for creating the output table: https://www.youtube.com/watch?v=B9BRuhqEb2Q
        
def dispay_earth_table_dictionary(earth_primary , earth_secondary , earth_melee ):
    
    
    print("\t\t\tPrimary weapons")
    print("-" *58)
    print("          Weapon           : Status     : Category : Location :\n")

    x=1
    for key, value in earth_primary.items():
        
        status = value["Status"] # assign variables to the value in the dictionary 
        category = value["Category"]
        location = value["Location"]
        
        print(f"{x}.)", key, ' '*(21-len(key)),':',
               status, ' '*(3-len(status)),':',
               category,' '*(2-len(category)),':',
               location,' '*(7-len(location)),':')
        x +=1

    print()
    print("\t\t\t Secondary weapons")
    print("-" *58)
    print("           Weapon            : Status     : Category   : Location :\n")

    
    for key, value in earth_secondary.items():
        
        status = value["Status"] # assign variables to the value in the dictionary 
        category = value["Category"]
        location = value["Location"]
        
        print(f"{x}.)", key, ' '*(22-len(key)),':',
               status, ' '*(3-len(status)),':',
               category,' '*(1-len(category)),':',
               location,' '*(6-len(location)),':')
        x+=1

    print()
    print("\t\t\t Melee weapons")
    print("-" *58)
    print("       Weapon            : Status     : Category : Location :\n")

    
    for key, value in earth_melee.items():
        
        status = value["Status"] # assign variables to the value in the dictionary 
        category = value["Category"]
        location = value["Location"]
        
        print(f"{x}.)" ,key, ' '*(18-len(key)),':',
               status, ' '*(3-len(status)),':',
               category,' '*(7-len(category)),':',
               location,' '*(7-len(location)),':')
        x+=1
    
#calculating  
def calculating_status_E(earth_primary , earth_secondary , earth_melee):

    not_found_P=[]#creates lists
    not_found_S=[]
    not_found_M=[]

    collceted_P=[]
    collceted_S=[]
    collceted_M=[]

    total_primary = len(earth_primary)  # Track total number of primary weapons
    total_secondary = len(earth_secondary)  # Track total number of secondary weapons
    total_melee = len(earth_melee)  # Track total number of melee weapons

    for values in earth_primary.values():
        if values['Status']=="not found":
          not_found_P.append(1)
        elif values['Status']== "collected":
            collceted_P.append(1)

    for values in earth_secondary.values():
        if values['Status']=="not found":
          not_found_S.append(1)
        elif values['Status']== "collected":
            collceted_S.append(1)
            
    for values in earth_melee.values():
        if values['Status']=="not found":
          not_found_M.append(1)
        elif values['Status']== "collected":
            collceted_M.append(1)
        
    print("you have collected" , len(collceted_P),"/",total_primary ,
          "primaries from earth")
    print("you have collected" , len(collceted_S),"/",total_secondary ,
          "Secondaries from earth")
    print("you have collected" , len(collceted_M),"/",total_melee,
          "Melee's from earth")


def user_select(earth_primary , earth_secondary , earth_melee):
    length = len(earth_primary.keys())+len(earth_secondary.keys())+len(earth_melee.keys())
    
    while True:
            try:                  
                answer=int(input("enter the number of the weapon status you want ot change: "))
                if 1<= answer <= length :
                    return answer
                else:
                    print(f"enter a valid number between 1-{length}") 
            except ValueError:
                print(f" enter a valid number")

                
def changing_status(earth_primary , earth_secondary , earth_melee):
    #display table
    dispay_earth_table_dictionary(earth_primary , earth_secondary , earth_melee )

    
    #get user number of weapon to change
    user_opt =user_select(earth_primary , earth_secondary , earth_melee)
    #convert to index
    user_index= user_opt-1


    #get user input
    user_status=update_status_primary(earth_primary, earth_secondary , earth_melee)
    
    primary_key=list(earth_primary.keys())
    secondary_key=list(earth_secondary.keys())
    melee_key=list(earth_melee.keys())

    if user_index < len(earth_primary):
        key = list(earth_primary.keys())[user_index]
        earth_primary[key]['Status'] = user_status
    elif user_index < len(earth_primary) + len(earth_secondary):
        key = list(earth_secondary.keys())[user_index - len(earth_primary)]
        earth_secondary[key]['Status'] = user_status
    else:
        key = list(earth_melee.keys())[user_index - len(earth_primary) - len(earth_secondary)]
        earth_melee[key]['Status'] = user_status

    save_changes( earth_primary, earth_secondary , earth_melee)

         

def save_changes(earth_primary, earth_secondary , earth_melee):

    with open("earth items.txt", "w") as file:
        for key, values in earth_primary.items():
            file.write(f"{key},{values['Status']},{values['Category']},{values['Location']}\n")
        for key, values in earth_secondary.items():
            file.write(f"{key},{values['Status']},{values['Category']},{values['Location']}\n")
        for key, values in earth_melee.items():
            file.write(f"{key},{values['Status']},{values['Category']},{values['Location']}\n")
           
    

   
def update_status_primary(earth_primary, earth_secondary , earth_melee):
    
    #error handler if user tries to display without creating chart
    if len(earth_primary) == 0 and len(earth_secondary) == 0 and len(earth_melee) == 0:
        print("Earth items not initialized")
        return
    
    
    
    

    while True:
        try:
            user_status=int(input("Enter 1 for 'collecteted' or 2 for 'not found': "))
            if user_status == 1:
                return "collected"
                
            elif user_status == 2:
                return "not found"
            else:
                print("invalid input, must be 1 or 2")
            
        except ValueError:
            print("invalid input, must be a whole number")


#min and max calulations

def min_stat(earth_primary, earth_secondary, earth_melee):
   
    primaries = len(earth_primary)
    secondaries = len(earth_secondary)
    melees = len(earth_melee)

    #disctionary
    category_counts = {
        'Primary': primaries,
        'Secondary': secondaries,
        'Melee': melees
    }

    max_category = max(category_counts, key=category_counts.get)
    min_category = min(category_counts, key=category_counts.get)
    
    
    print(f"The category with the most weapons is {max_category} with {category_counts[max_category]} weapons.")
    print(f"The category with the least weapons is {min_category} with {category_counts[min_category]} weapons.")

#error handler
def inializing_file_error():
    
    print("Are you sure you want to initialize the file? This will wipe any saved completion.")
    user_input = input("If yes, type 'yes' to continue, or enter anything to cancel: ")

    if user_input.lower() == 'yes':
        print("Earth Item initialized")
        return True
        
    else:
        return False
        
import tkinter 

#Dynamic menus 
def main_menu():

   
    main_window = tkinter.Tk()#make the window gui thingy
    main_window.title("User interface log")#title the screen

    # Create a Label to display messages
    main_window.geometry("400x200")
    output_label = tkinter.Label(main_window, text='Welcome to the Remnant 2 Item Tracker!', justify='left')
    output_label.pack()
    
    print("Welcome to the Remenant 2 Item list tracker\n")
    print()
   

    earth_primary, earth_secondary, earth_melee = create_earth_dictionary()
    
    loop = True #defines a true and false statement to keep displaying the menu
    while loop:
        
        main_window.update()
        
        print()
        print("1. initialize earth Items ")
        print("2. Display Items ")
        print("3. update status")
        print("4. earth stats")
        print("5. quit")
        
        try:
            menu = int(input("Enter a number 1-5: "))  
        except ValueError:
            print(f"Not an option at this time")
            continue
        
       
        
        if menu == 1:
            output_label.config(text="You selected: Initialize Earth Items")
            if inializing_file_error():
                # Initialize the list
                create_folder()
                earth_primary_list, earth_secondary_list, earth_melee_list = parse_folder()
                basic_operations(earth_primary_list, earth_secondary_list, earth_melee_list)
                # Create the dictionary
                create_CSV_earth(earth_primary_list, earth_secondary_list, earth_melee_list)
                earth_primary, earth_secondary, earth_melee = create_earth_dictionary()
            else:
                print("File initialization canceled.")

        elif menu == 2:
            if read_file():
                output_label.config(text="Items displayed.")
                calculating_status_E(earth_primary, earth_secondary, earth_melee)
            else:
                output_label.config(text="No items to display.")

        elif menu == 3:
            if read_file():
                changing_status(earth_primary, earth_secondary, earth_melee)
                output_label.config(text="Status updated.")
            else:
                output_label.config(text="No items to update.")

        elif menu == 4:
            if read_file():
                min_stat(earth_primary, earth_secondary, earth_melee)
                output_label.config(text="Displaying stats.")
            else:
                output_label.config(text="No stats to display.")

        elif menu == 5:
            output_label.config(text="You selected: Quit")
            print("Goodbye")
            loop = False
        else:
            print("Not an option at this time")

    # Destroy the main window after the loop ends
    main_window.destroy()



def main():
    main_menu()

main()

