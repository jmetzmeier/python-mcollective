"""
:py:mod:`pymco.connector.stomp`
"""
from . import Connector


class StompConnector(Connector):
    def get_target(self, agent, collective):
        """Implement :py:meth:`pymco.connector.Connector.get_target`"""
        return '{topic_prefix}{collective}.{agent}.command'.format(
            agent=agent,
            collective=collective,
            topic_prefix=self.config['topicprefix'],
        )

    def get_reply_target(self, agent, collective):
        """Implement :py:meth:`pymco.connector.Connector.get_reply_target`"""
        return '{topic_prefix}{collective}.{agent}.reply'.format(
            agent=agent,
            collective=collective,
            topic_prefix=self.config['topicprefix'],
        )
