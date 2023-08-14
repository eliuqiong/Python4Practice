def formatted_name(first_name, last_name):
    """return a well-formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("please enter your nanme, and you will get well formatted name")
    print("\nif you want to quit, simple enter 'q'")
    
    first_name = input("your first name is ? Enter here: ")
    if first_name == "q":
        break

    last_name = input("your last name is ? Enter here: ")
    if last_name == "q":
        break    

    well_format_name = formatted_name(first_name, last_name)
    print(f"here is a well formatted name of you: {well_format_name}")
