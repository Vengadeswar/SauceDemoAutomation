#pytest expects as a list of values or tuple of values

valid_creds = [
    {"username": "visual_user", "password": "secret_sauce"},
    {"username": "standard_user", "password": "secret_sauce"}
]

invalid_username_creds = {"username":"visual","password":"secret_sauce"}

invalid_password_creds = {"username":"visual_user","password":"secret"}