import functools

user = {"username": "jose", "access_level": "guest"}


# decorator function:
def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        print(*args)
        print(**kwargs)
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password.__name__)
print(get_admin_password())

user = {"username": "jose", "access_level": "admin"}
print(get_admin_password())


# decorator function with parameter:
@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print(get_password("admin"))
print(get_password("billing"))

