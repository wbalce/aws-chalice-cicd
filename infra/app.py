import os
from aws_cdk import core as cdk
from stacks.main_app import MainApp

app = cdk.App()

dev_env = cdk.Environment(
    account=os.environ['CDK_DEFAULT_ACCOUNT'],
    region=os.environ['CDK_DEFAULT_REGION'])

MainApp(app, 'MainAppDev', env=dev_env)

app.synth()
