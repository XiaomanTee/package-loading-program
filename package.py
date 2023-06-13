items = int(input("Enter the maximun number of items to be shipped: "))

current_weight = 0
number_of_package_sent = 0
total_weight_of_packages_sent = 0
total_unused_capacity = 0
most_unused_capacity_package = 0
amount_unused_capacity_in_package = 0
current_unused_capacity = 0

for i in range(items):
    weight = input("Enter the weight of item{}: ".format(i+1))
    
    if weight == '0':
        break
    elif not weight.isdigit():
        print("Invalid weight. Please enter the valid weight by number.")
        continue

    weight = int(weight)
    
    if weight < 1 or weight > 10:
        print("Error input. Please enter the weight between 1kg to 10kg.")
        continue

    total_weight_of_packages_sent += weight

    if current_weight + weight > 20:
        number_of_package_sent += 1
        current_unused_capacity = 20 - current_weight

        if current_unused_capacity > amount_unused_capacity_in_package:
            amount_unused_capacity_in_package = current_unused_capacity
            most_unused_capacity_package = number_of_package_sent

        current_weight = weight
    else:
        current_weight += weight

if current_weight > 0:
    number_of_package_sent += 1
    current_unused_capacity = 20 - current_weight

    if current_unused_capacity > amount_unused_capacity_in_package:
        amount_unused_capacity_in_package = current_unused_capacity
        most_unused_capacity_package = number_of_package_sent

total_unused_capacity = number_of_package_sent * 20 - total_weight_of_packages_sent

print("\n******************************")
print(f"Number of packages sent: {number_of_package_sent}")
print(f"Total weight of packages sent: {total_weight_of_packages_sent}")
print(f"Total 'unused' capacity: {total_unused_capacity}")
print(f"The package number that had most 'unused' capacity: {most_unused_capacity_package}")
print(f"The amount of 'unused' capacity in the package: {amount_unused_capacity_in_package}")
print("********************************")


