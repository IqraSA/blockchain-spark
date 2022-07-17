class TypeNotSupported(Exception):
    """
    We failed to decode ABI type to Spark type
    """

    def __init__(self, type_str: str) -> None:
        message = f"Solidity type not supported: {type_str}"
        super().__init__(message)


class ABITypeNotValid(Exception):
    """
    We failed to create ABI type
    """

    def __init__(self, message) -> None:
        super().__init__(message)
