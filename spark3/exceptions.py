from pyspark.sql import DataFrame


class FailToGetEtherscanABI(Exception):
    """
    We failed to get ABI from Etherscan
    """
    def __init__(self, message) -> None:
        super().__init__(message)


class ColumnNotFoundInDataFrame(Exception):
    """
    We failed to find columns in a Dataframe
    """

    def __init__(self, name: str, df: DataFrame) -> None:
        message = f"Column {name} not found in DataFrame: {df.schema.simpleString()}"
        super().__init__(message)


class ContractABINotConfigured(Exception):
    """
    We failed to find abi json in contract
    """

    def __init__(self, message) -> None:
        super().__init__(message)


class ABIFunctionNotFound(Exception):
    """
    We failed to find function ABI
    """

    def __init__(self, message) -> None:
        super().__init__(message)


class ABIEventNotFound(Exception):
    """
    We failed to find event ABI
    """

    def __init__(self, message) -> None:
        super().__init__(message)

