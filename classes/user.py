class User(object):
    def __init__(self, 
                 id:str, 
                 pwd:str, 
                 email:str, 
                 is_signed_in:bool = False, 
                 is_new:bool = True) -> None:
        self._id = id
        self._pwd = pwd
        self._email = email
        self._is_signed_in = is_signed_in
        self._is_new = is_new

    def signin(self) -> None:
        self.set_is_signed_in(True)

    def get_id(self) -> str:
        return self._id

    def get_pwd(self) -> str:
        return self._pwd

    def get_email(self) -> str:
        return self._email

    def get_is_signed_in(self) -> bool:
        return self._is_signed_in

    def get_is_new(self) -> bool:
        return self._is_new

    def set_id(self, id:str) -> None:
        self._id = id

    def set_pwd(self, pwd:str) -> None:
        self._pwd = pwd

    def set_email(self, email:str) -> None:
        self._email = email

    def set_is_signed_in(self, is_signed_in:bool) -> None:
        self._is_signed_in = is_signed_in

    def set_is_new(self, is_new:bool) -> None:
        self._is_new = is_new