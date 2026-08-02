def create_user(name, age, country):
    """
    Create a user dictionary with name, age, and country.

    Args:
        name (str): User's name
        age (int): User's age
        country (str): User's country

    Returns:
        dict: Dictionary containing user information
    """
    user = {
        "name": name,
        "age": age,
        "country": country
    }
    return user


def count_users_by_country(users_list):
    """
    Count the number of users from each country.

    Args:
        users_list (list): List of user dictionaries

    Returns:
        dict: Dictionary with countries as keys and user counts as values
    """
    country_counts = {}
    for user in users_list:
        country = user['country']
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1
    return country_counts


def get_max_age(users_list):
    """
    Find the user(s) with the maximum age.

    Args:
        users_list (list): List of user dictionaries

    Returns:
        tuple: (max_age, list_of_users_at_max_age)
    """
    if not users_list:
        return None, []

    max_age = max(user['age'] for user in users_list)
    users_at_max_age = [user for user in users_list if user['age'] == max_age]
    return max_age, users_at_max_age


def display_user_list(users_list):
    """
    Display all users in a formatted way.

    Args:
        users_list (list): List of user dictionaries
    """
    print("\n" + "=" * 60)
    print("USER DIRECTORY")
    print("=" * 60)

    if not users_list:
        print("No users found.")
        return

    for i, user in enumerate(users_list, 1):
        print(f"{i}. {user['name']:15} | Age: {user['age']:3} | Country: {user['country']:12}")

    print("=" * 60)


def analyze_users(users_list):
    """
    Analyze user data by country and age.
    """
    print("\n" + "=" * 60)
    print("COUNTRY SUMMARY")
    print("=" * 60)

    country_counts = count_users_by_country(users_list)
    for country, count in sorted(country_counts.items()):
        bar = "█" * count
        print(f"{country:15} : {count:2} {bar}")

    max_age, oldest_users = get_max_age(users_list)

    print(f"\n👑 OLDEST USER(S):")
    print("-" * 40)
    if oldest_users:
        print(f"Maximum Age: {max_age} years")
        print("Users at this age:")
        for user in oldest_users:
            print(f"  • {user['name']} from {user['country']}")
    else:
        print("No users found.")

    print(f"\n📈 STATISTICS:")
    print("-" * 40)
    ages = [user['age'] for user in users_list]
    print(f"Total users : {len(users_list)}")
    if ages:
        print(f"Average age : {sum(ages) / len(ages):.1f} years")
        print(f"Age range   : {min(ages)} - {max(ages)} years")
    else:
        print("Average age : 0.0 years")
        print("Age range   : 0 - 0 years")
    print("=" * 60)


def main():
    """
    Main function to demonstrate creating and manipulating user data.
    """
    print("\n" + "=" * 60)
    print("   USER DATA STRUCTURE EXERCISE")
    print("=" * 60)

    users = []

    print("\nCreating users...")
    users.append(create_user("Alice Johnson", 28, "USA"))
    users.append(create_user("Bob Smith", 35, "Canada"))
    users.append(create_user("Carlos Garcia", 42, "Mexico"))
    users.append(create_user("Diana Patel", 31, "India"))
    users.append(create_user("Elena Kim", 28, "South Korea"))

    users.append(create_user("Frank Wilson", 55, "USA"))
    users.append(create_user("Grace Okafor", 29, "Nigeria"))
    users.append(create_user("Hiro Tanaka", 42, "Japan"))
    users.append(create_user("Isabella Rossi", 35, "Italy"))

    display_user_list(users)
    analyze_users(users)

    print("\n" + "=" * 60)
    print("   DATA MANIPULATION DEMONSTRATION")
    print("=" * 60)

    print("\nUsers from USA:")
    usa_users = [user for user in users if user['country'] == 'USA']
    for user in usa_users:
        print(f"  • {user['name']} (Age: {user['age']})")

    print("\nUsers sorted by age (youngest to oldest):")
    sorted_users = sorted(users, key=lambda x: x['age'])
    for user in sorted_users:
        print(f"  • {user['name']:15} | Age: {user['age']:3} | Country: {user['country']}")

    print("\nUpdating user information...")
    for user in users:
        if user['name'] == "Alice Johnson":
            user['age'] = 29
            print(f"✓ Updated Alice's age to {user['age']}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
