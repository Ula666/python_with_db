import requests


url = "https://openlibrary.org/books/"
books = input("Please enter book id ")
url_arg = url + books
print(url_arg)

# to check status code
response = requests.get(url_arg)
print(response.status_code)


class NewBooks:
    def __init__(self):
        response_dict = response.json()
        response_keys = response_dict["result"]
        pass


    def retrieve_info(self):
        pass

    def display_info(self):
        pass
