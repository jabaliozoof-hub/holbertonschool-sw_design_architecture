#!/usr/bin/env python3
"""
1-observer.py: Implementing SmsObserver and subscribing to breaking news.
"""


class NewsSubject:
    """Subject that broadcasts news to observers."""

    def __init__(self):
        self._observers = []

    def subscribe(self, observer, topics=None):
        """Subscribe an observer to specific topics."""
        self._observers.append((observer, set(topics) if topics else None))

    def unsubscribe(self, observer):
        """Unsubscribe an observer."""
        self._observers = [
            item for item in self._observers if item[0] != observer
        ]

    def notify(self, topic: str, data: str):
        """Notify all matching observers about an event."""
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Observer that logs events."""

    def update(self, topic: str, data: str):
        print(f"log:{topic}={data}")


class EmailObserver:
    """Observer that sends emails for events."""

    def update(self, topic: str, data: str):
        print(f"email:{topic}={data}")


class SmsObserver:
    """Observer that sends SMS alerts."""

    def update(self, topic: str, data: str):
        print(f"sms:{topic}={data}")


def main():
    news = NewsSubject()

    log_obs = LogObserver()
    email_obs = EmailObserver()
    sms_obs = SmsObserver()

    news.subscribe(
        log_obs,
        topics={"sports", "breaking"}
    )
    news.subscribe(email_obs)
    news.subscribe(
        sms_obs,
        topics={"breaking"}
    )

    news.notify("weather", "rain")
    news.notify("sports", "goal")
    news.notify("breaking", "alert")


if __name__ == "__main__":
    main()
