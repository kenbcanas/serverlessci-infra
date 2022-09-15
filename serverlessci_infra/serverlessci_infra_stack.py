from aws_cdk import (
    App,
    Stack,
    aws_fsx as _fsx
)


class ApplicationStack(Stack):

    def __init__(self, scope: App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        wsLustreFs = _fsx.LustreFileSystem(self, "wsLustreFs",
            storage_capacity_gib=1200
        )
