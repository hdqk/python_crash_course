# Hector Delgado 5/8/2024

def build_profile(first, last, **user_info):
    """build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('hector', 'delgado', location='santo domingo',
                             age=35, field='software engineer')

print(user_profile)
