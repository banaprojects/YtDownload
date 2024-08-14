credentials = []
with open('config.txt', 'r') as f:
    for line in f:
        credentials.append(line.strip())

# print(credentials)

username, password = credentials
print(username)
print(password)