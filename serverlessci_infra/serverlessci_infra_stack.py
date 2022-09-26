from aws_cdk import (
    App,
    Stack,
    aws_fsx as _fsx,
    aws_ec2 as _ec2,
)


class ApplicationStack(Stack):

    def __init__(self, scope: App, construct_id: str, **kwargs) -> None:
        stack_config = kwargs['stack_config']
        kwargs.pop('stack_config',None)
        print(stack_config)

        super().__init__(scope, construct_id, **kwargs)

        print(stack_config)

        compute_vpc = _ec2.Vpc.from_lookup(self, "ComputeVPC",
            vpc_id = stack_config['vpc.id']
        )

        compute_subnet = _ec2.Subnet.from_subnet_id(self,"FSXSubnet",stack_config['vpc.subnet.id'])
 
        wsLustreFsConifg = {
            "deployment_type": _fsx.LustreDeploymentType.SCRATCH_2,
        }
            # "export_path": bucket.s3_url_for_object(),
            # "import_path": bucket.s3_url_for_object(),
            # "auto_import_policy": fsx.LustreAutoImportPolicy.NEW_CHANGED_DELETED

        wsLustreFs = _fsx.LustreFileSystem(self, "wsLustreFs",
            storage_capacity_gib=1200,
            vpc = compute_vpc,
            vpc_subnet = compute_subnet,
            lustre_configuration = wsLustreFsConifg
        )
