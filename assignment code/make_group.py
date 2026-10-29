import random


# Takes a list of student names
# Uses random.shuffle() to randomize the order
# Returns the shuffled list
# Don’t forget import random at the top
def shuffle_list(items):
    random.shuffle(items)
    return items

# make_groups(shuffled_list, num_groups, prefix)
# Takes the shuffled list, number of groups, and prefix
# Splits students as evenly as possible across the groups
# Returns a dictionary where:Keys are group names like "Team 1", "Team 2"
# Values are lists of student names in that group
#def make_groups(shuffle_list, num_groups, prefix ):
    
    

#A string of student names separated by commas
# Number of groups to create
# A prefix for group names, like "Team" or "Group"
#names = ["Lazio", "Mary", "Micheal", "Rose"]
names_input = input("Enter the names of the students separated by a comma\n")
names = [name.strip() for name in names_input.split(',')]

shuffle_name = shuffle_list(names)
print(shuffle_name)

# num_groups = input("Enter the number of groups you want to create")
# prefix = input("Enter if you want Team, group or any other tag name, no number allowed")
