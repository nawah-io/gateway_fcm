# Nawah Gateway for Firebase Cloud Messaging (FCM)
This repo is a [Nawah](https://github.com/nawah-io/nawah_docs) Package that allows developers to integrate [FCM](https://firebase.google.com/docs/cloud-messaging) into Nawah apps using Gateway Controller.

## How-to
1. From your app directory run: `nawah packages add gateway_fcm`
2. Add `fcm` Var to `nawah_app.py` App Config:
```python
vars = {
    'fcm': {'token': 'FCM_API_TOKEN'}
}
```
3. `fcm` gateway requires following arguments:
   1. `registration_id`: Target device registration identifier. Type `str`.
   2. `message_title`: Message title. Type `str`.
   3. `message_body`: Message body. Type `str`.
   4. `data_message`: Additional payload data to be sent with the message. Type `dict`.
4. `fcm` gateway accepts optional argument, namely `fcm_auth`, replicating `fcm ` for dynamic FCM API credentials.
5. Use `fcm` gateway using Nawah Gateway Controller:
```python
from nawah.gateway import Gateway

Gateway.send(gateway='fcm', registration_id=registration_id, message_title=message_title, message_body=message_body, data_message=data_message)
```