import requests

class NewBooks:
    def __init__(self):
        pass





# OL7353617M

        #response_dict = response.json()
        #response_keys = response_dict["result"]

    def retrieve_info(self):
        url = "https://openlibrary.org/books/"
        books = input("Please enter book id ")
        url_arg = url + books
        # to check status code
        response = requests.get(url_arg)
        print(response.status_code)
        print(url_arg)

    def display_info(self):
        pass



    # for items in response_dict.keys():
    #     if items == "key":
    #         print("Your book is " + str(response_keys["books"]))