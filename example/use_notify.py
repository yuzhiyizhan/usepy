from usepy.integrations.useNotify import useNotify, useChannels

notify = useNotify()
notify.add(
    useChannels.Bark({"token": "jtgTe64kJAtq4iyj6DaepQ"}),
)

notify.publish(content="usepy")
