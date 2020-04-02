# Use while loop to print numbers between the number to start on and number to end on by prompting the user.

start_num = input('Please tell me the number to start on ')
end_num = input('Please tell the number to end on ')
count = int(start_num)
while count <= int(end_num):
    print(count)
    count = count + 1
