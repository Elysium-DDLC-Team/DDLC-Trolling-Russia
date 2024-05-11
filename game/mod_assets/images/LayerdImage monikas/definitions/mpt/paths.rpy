
init -200 python:

    from multipledispatch import dispatch

    class Paths:

        _base_path = "mod_assets/images"
        _file_format = "png"

        @dispatch(str, str)
        def nsmonika(self, part: str, filename:str) -> str:
            return f"{self._base_path}/Non-Sentient Monika/{part}/{filename}.{self._file_format}"

        @dispatch(str, str, str)
        def nsmonika(self, part: str, type: str, filename:str) -> str:
            return f"{self._base_path}/Non-Sentient Monika/{part}/{type}/{filename}.{self._file_format}"


    paths = Paths()

