from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if re.match("^[a-z]+$", username):
            pass
        else:
            raise UserInputError("Username should only contain letters")

        if len(username) >= 3:
            pass
        else:
            raise UserInputError("Username too short")

        if re.match("^[a-zA-Z*]+[0-9]|[0-9]+$", password):
            pass
        else:
            raise UserInputError("Password contains only letters")        

        if len(password) >= 8:
            pass
        else:
            raise UserInputError("Password too short")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
