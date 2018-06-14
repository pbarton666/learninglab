#py_misc_string_ops.py
my_team = "The Chicago Cubs"

split_team = my_team.split(" ")
print("splits:  {}".format(split_team))

#Note the use of the optional 'end= argument to print().  The
# signature looks like print(value= '', sep = ' ', end = '\n' ...)
join_string="!!!"
together_again = join_string.join(split_team)
print("together again: {}".format( together_again), end=join_string+"\n")



