def string_to_array(string):
  string1 = string.split(" ")
  print(string1)


string_to_array("Robin Singh") #["Robin" "Singh"]
string_to_array("CodeWars") #["CodeWars"]
string_to_array("I love arrays they are my favourite") 
#["I", "love", "arrays", "they", "are", "my", "favourite"]
string_to_array("1 2 3") #["1", "2", "3"]
string_to_array("") # returns []