"""

- define a class CustomSet
    - define an init method to take a default dictionary 
        - initialize self.members to dictionary where each element in the list is a key and value is True

    - define an instance method is_empty
        - return if dictionary is not truthy

    - define an instance method contains, with 1 number
        - return if number is in self.members

    - define an instance method is_subset with 1 list 
        - return if all elements in self.members is in other.members

    - define an instance method is_disjoint, with 1 instance of CustomSet
        - return if all self.members are not in the other.members  

    - define an instance method is_same with 1 list 
        - return if self.members.keys() is equal to other.members.keys()
    
    - define an instance method add with 1 number
        - add number to key/value pair of members dictionary 

    - define an instance method intersection with 1 instance of CustomSet
        - initialize a dictionary 
        - iterate over self.members
            - if key in other.members
                - create a key/value pair

        - return dictionary as a new CustomSet object

    - define an instance method difference with 1 instance of CustomSet
        - initialize a dictionary
        - iterate over self.members
            - if key not in other.members
                - create key/value pair 

        - return dictionary as a new CustomSet object
    
    - define an instance method union with 1 instance
        - merge both dictionaries
        - return dictionary as a new CustomSet object

"""

class CustomSet:
    def __init__(self, members=None):
        if members:
            self.members = {member: True for member in members}
        else:
            self.members = {}
        
    def __eq__(self, other):
        return self.members == other.members
    
    def is_empty(self):
        return not self.members 
    
    def contains(self, member):
        return member in self.members
    
    def is_subset(self, other):
        return all(member in other.members for member in self.members)
    
    def is_disjoint(self, other):
        return all(member not in other.members for member in self.members)
    
    def is_same(self, other):
        return self.members.keys() == other.members.keys()
    
    def add(self, member):
        self.members[member] = True

    def intersection(self, other):
        intersection_set = {member: True for member in self.members if member in other.members}
        return CustomSet(intersection_set)
    
    def difference(self, other):
        difference_set = {member: True for member in self.members if member not in other.members}
        return CustomSet(difference_set)
    
    def union(self, other):
        union_set = self.members | other.members
        return CustomSet(union_set)
