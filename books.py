import requests


class NewBooks:
    def __init__(self):
        self.url = "https://openlibrary.org/books/"
        self.greetings()
        self.books = input("Please enter book id that you're interested in: ")
    # use this id to check: OL7353617M


    def greetings(self):
        print("Hello User!")


    def check_status(self):
        url_arg = self.url + self.books
        print(url_arg)
        status = requests.get(url_arg).status_code
        if status == 200:
            print("The website is running, and the status code is: " + str(status))
        else:
            print("Something wrong")


book = NewBooks()
book.greetings()
book.check_status()
