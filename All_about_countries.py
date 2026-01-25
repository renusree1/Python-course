class India:
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Many languages are spoken in India but Hindi is the most widely spoken language")
    def type(self):
        print("India is a developing country")
class USA:
    def capital(self):
        print("Washington is the capital of USA")
    def language(self):
        print("The primary language spoken in the USA is English")
    def type(self):
        print("USA is a developed country")

obj_india= India()
obj_usa= USA()

for country in (obj_india, obj_usa):
    country.capital()
    country.language()
    country.type()