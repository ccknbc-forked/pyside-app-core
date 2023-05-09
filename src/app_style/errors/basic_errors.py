class CoreError(Exception):
    """base error for application"""

    @property
    def internal(self) -> bool:
        return self._internal

    def __init__(self, msg: str, internal=False):
        self._internal = internal
        super(CoreError, self).__init__(msg)
