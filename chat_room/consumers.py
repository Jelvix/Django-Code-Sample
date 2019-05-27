import json

from channels.channel import Group

from chat_room.models import Message


def get_room_id(message):
    return message.content.get('path').replace('/', '')


def ws_connect(message, room_id):
    # room_id = id
    message.reply_channel.send({"accept": True})
    Group(room_id).add(message.reply_channel)


def ws_message(message, room_id):
    # room_id = get_room_id(message)
    data = json.loads(message.content['text'])
    msg_obj = Message.objects.create(text=data['text'], sender_id=data['sender_id'], room_id=room_id)
    Group(room_id).send({
        'text': json.dumps({
            'text': msg_obj.text, 'sender': str(msg_obj.sender), 'sender_id': data['sender_id'],
            'creation_date': str(msg_obj.creation_date.strftime("%b. %d,  %Y, %I:%M.%p"))
        })
    })


def ws_qwe(message):
    Group('qwe').send({
        'text': 'hitgbbrtvg5tg'
    })


def ws_qwe_connect(message):
    message.reply_channel.send({"accept": True})
    Group('qwe').add(message.reply_channel)


def ws_qwe_disconnect(message):
    Group('qwe').discard(message.reply_channel)


def ws_disconnect(message, room_id):
    # room_id = get_room_id(message)
    Group(room_id).discard(message.reply_channel)
