import logging

logger = logging.getLogger(__name__)


def create_endpoint(context):
    endpoint = {
        url: 'https://demo.resouces',
        user: 'scotty',
        password: '********',
    }
    return endpoint


def deploy(context):
    name = context.v1.self.name
    print 'Hey there,'
    print 'my name is {name} '.format(name=name),
    print 'and I\'m deploy a dummy resource with my config:'
    print '{config}'.format(config=context.v1.self.config)