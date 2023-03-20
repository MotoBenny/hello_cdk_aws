import aws_cdk as core
import aws_cdk.assertions as assertions

from hello_cdk_aws.hello_cdk_aws_stack import HelloCdkAwsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in hello_cdk_aws/hello_cdk_aws_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HelloCdkAwsStack(app, "hello-cdk-aws")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
