from prettytable import PrettyTable

t1 = PrettyTable(["ENR", "Name", "City"])
t1.add_row(["1915010155", "Gaurav", "Aurangabad"])
t1.add_row(["1915010165", "Ajinkya", "Aurangabad"])
t1.add_row(["1915010199", "Pratham", "Aurangabad"])
print(t1)