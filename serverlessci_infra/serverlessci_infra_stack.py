from aws_cdk import (
    App,
    Stack,
    aws_fsx as _fsx
)


class ApplicationStack(Stack):

    def __init__(self, scope: App, construct_id: str, **kwargs) -> None:
        stack_config = kwargs['stack_config']
        kwargs.pop('stack_config',None)
        print("XXXXXXXXXX-----------")
        print(stack_config)
        print("XXXXXXXXXX-----------")

        super().__init__(scope, construct_id, **kwargs)

        print("XXXXXXXXXX-----------")
        print(stack_config)
        print("XXXXXXXXXX-----------")
#       wsLustreFs = _fsx.LustreFileSystem(self, "wsLustreFs",
#            storage_capacity_gib=1200
#        )
