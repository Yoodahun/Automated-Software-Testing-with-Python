from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    """
    Function that gets called when a user calls the /authenticate endpoint
    with the username and password.
    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

    return None

def identity(payload):
    """
    Function that gets called when user has already authenticated, logged in and Flask-JWT
    verified thier authorization header is correct
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

