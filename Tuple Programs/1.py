def domain(email):
    username, domain = email.split('@')
    return username, domain
email_ad = input("Enter your Email :")
username, domain = domain(email_ad)
print("User name:", username)
print("Domain name:", domain)
