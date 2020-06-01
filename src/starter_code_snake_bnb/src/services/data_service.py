from data.owners import Owner

def create_account(name: str, email: str) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email

    owner.save() # primary key auto generated

    return owner

def find_account_by_email(email: str) -> Owner:
    owner = Owner.objects(email = email).first() # returns query
    return owner

