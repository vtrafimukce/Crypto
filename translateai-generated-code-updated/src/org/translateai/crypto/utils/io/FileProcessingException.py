class FileProcessingException(Exception):
    def __init__(self, message, cause=None):
        super().__init__(message, cause)