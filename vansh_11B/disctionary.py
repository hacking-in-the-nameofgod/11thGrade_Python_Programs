branches = {"CS": 120, "EC": 100, "EE": 60, "ME": 50, "CE": 40, "CH": 50}

while True:
  choice = int(input("1) Add branch, 2) Allot seat, 3) Remove branch, 4) List branches, 5) Exit: "))
  if choice == 1:
    new_branch = input("Enter new branch name: ").upper()
    while new_branch in branches:
      new_branch = input("Branch exists, enter another: ")
    seats = int(input("Number of seats: "))
    branches[new_branch] = seats
    
  elif choice == 2:
    name = input("Candidate name: ")
    branch = input("Branch: ").upper()
    while branch not in branches or branches[branch] == 0:
      if branch not in branches:
        print("Branch doesn't exist!")
      else:
        print("Branch full!")
      branch = input("Enter another branch: ").upper()
    branches[branch] -= 1
    if branches[branch] == 0:
      del branches[branch]
      print(f"Branch '{branch}' full and removed!")
    print(f"Seat allotted to {name} in {branch}!")
  elif choice == 3:
    branch = input("Remove branch: ").upper()
    while branch not in branches:
      print("Branch doesn't exist!")
      branch = input("Enter another branch: ").upper()
    del branches[branch]
    print(f"Branch '{branch}' removed!")
  elif choice == 4:
    print("-" * 30)
    print("Branch\t\tSeats")
    print("-" * 30)
    for branch, seats in branches.items():
      print(f"{branch}:\t\t{seats}")
    print("-" * 30)
  elif choice == 5:
    break
  else:
    print("Invalid choice!")

print("Program terminated.")
