#!/usr/bin/env python3

import sys
from aws_cdk import (
    App,
    Environment as _environment
)

from serverlessci_infra.serverlessci_infra_stack import ApplicationStack
from jproperties import Properties  

stack_config = {}
def loadProperties():
    default_configs = Properties()
    with open('conf/serverlessci-default.properties', 'rb') as read_prop:
        default_configs.load(read_prop)
      
    default_prop_view = default_configs.items()
    print(type(default_prop_view))
   
    for item in default_prop_view:
        print(item)
        stack_config[item[0]] = item[1].data
    print(stack_config)

    print("----")
    env_configs = Properties()
    with open('conf/serverlessci-blaugthon.properties', 'rb') as read_prop:
        env_configs.load(read_prop)
      
    env_prop_view = env_configs.items()
    print(type(env_prop_view))
   
    for item in env_prop_view:
        print(item)
        stack_config[item[0]] = item[1].data
    print(stack_config)



loadProperties()

serverless_ci_env = _environment(account=stack_config['aws.account'], region=stack_config['aws.region'])
app = App()
ApplicationStack(app, "cipipe-core-stack",
     stack_config=stack_config,
     env=serverless_ci_env
)

app.synth()
