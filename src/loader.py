class Loader:
    """Mix-in class for loading and unloading notegroup recipes from contents"""
    loaded_recipes: dict = {}

    def __init__(self, *args, **kwargs) -> None:
        """Loader doesn't have an __init__ of its own"""
        pass

    def __init_subclass__(cls) -> None:
        cls.loaded_recipes = dict()

    @classmethod
    def load_recipes(cls, contents: list[str]) -> None:
        """Loads a dictionary of labels and recipes from contents (e.g. text files)"""
        for a_line in contents:
            # TODO: proper failsafe (regex) for not matching patterns
            if a_line[0] == '#' or a_line[0] == '\n':
                pass
            else:
                label, *list_of_strings, = a_line.split()
                arg = [int(a_string) for a_string in list_of_strings]
                cls.loaded_recipes[label] = arg

    @classmethod
    def clear_recipes(cls) -> None:
        """Clears the loaded_recipes set"""
        cls.loaded_recipes.clear()

    @classmethod
    def get_recipes(cls) -> dict:
        """Returns the loaded_recipes set"""
        return cls.loaded_recipes
