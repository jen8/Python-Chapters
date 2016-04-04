class SMS_store:

    def __init__(self):
        self.store = []
    
    def __str__(self):
        return self.store.__str__()
    
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        message = (False, from_number, time_arrived, text_of_SMS)
        self.store.append(message)

    def message_count(self):
        return len(self.store)

    #BRIAN JUST WATCHES!!! ONLY ANSWER QUESTION. Hands to himself
    def get_unread_indexes(self):
        return 

    #BRIAN JUST WATCHES!!! ONLY ANSWER QUESTION. Hands to himself
    def get_message(self, i):
        return 

    def delete(self, i):
        del self.store[i]
    
    def clear(self):
        self.store.clear()
    

my_inbox = SMS_store()
print(my_inbox)
my_inbox.add_new_arrival(51075548, 853465756476, "hi")
my_inbox.add_new_arrival(546894, 453646754, "bye")
print(my_inbox)
print(my_inbox.message_count())
print(my_inbox.get_unread_indexes())
print("get_message(0):" + my_inbox.get_message(0).__str__())
print(my_inbox)
print(my_inbox.get_unread_indexes())
my_inbox.delete(0)     
print(my_inbox)
my_inbox.clear()       
print(my_inbox)

