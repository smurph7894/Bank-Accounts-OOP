class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0 

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount    
        else:
            print(f"{self.first_name} does not have enough points for this.")

    
sarah = user("Sarah", "Murphree", "murphs@dojo.com", 28)
beth = user("Beth", "Human", "Hums@email.com", 103)
roger = user("Roger", "Grig", "grig@email.com", 14)

sarah.enroll()
sarah.spend_points(50)
beth.enroll()
beth.spend_points(80)
sarah.display_info()
beth.display_info()
roger.display_info()
sarah.enroll()
roger.spend_points(40)

