import aws_cdk as core
import aws_cdk.assertions as assertions

from url_short.url_short_stack import UrlShortStack

# example tests. To run these tests, uncomment this file along with the example
# resource in url_short/url_short_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = UrlShortStack(app, "url-short")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
