#!/usr/bin/env python3

from aws_cdk import App

from serverlessci_infra.serverlessci_infra_stack import ApplicationStack


app = App()
ApplicationStack(app, "cipipe-core-stack")

app.synth()
