class Format:
    @staticmethod
    def Name(name:str) -> str:
        if ',' in name:
            lastName, firstName = name.split(", ")
            return f"{firstName} {lastName}"
        return name