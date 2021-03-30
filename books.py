import requests

class NewBooks:
    def __init__(self):
        self.greetings()
        self.retrieve_info()

        pass

    def greetings(self):
        print("Hello User!")



# OL7353617M

        #response_dict = response.json()
        #response_keys = response_dict["result"]

    def retrieve_info(self):
        #url = "https://openlibrary.org/books/"
        books = input("Please enter book id that you're interested in: ")
       # url_arg = url + books
        # to check status code
        #response = requests.get(url_arg)
        #print(response.status_code)
        print(books)

    def check_status(self):
        try:
            response = requests.get("https://openlibrary.org/books/")
            if response.status_code == 200:
                print("You can see the website")
                print(response.json())
            else:
                print("something wrong" + str(response.status_code))
        except Exception as e:
            raise("Error")


if __name__=='__main__':
    obj = NewBooks()


    # for items in response_dict.keys():
    #     if items == "key":
    #         print("Your book is " + str(response_keys["books"]))