# Ancora Imparo.

from nawah.classes import PACKAGE_CONFIG, ATTR
from nawah.registry import Registry

from typing import Dict, Any, TypedDict
from pyfcm import FCMNotification


def fcm_gateway(
	registration_id: str,
	message_title: str,
	message_body: str,
	data_message: Dict[str, Any],
	fcm_auth: TypedDict('GATEWAY_FCM_AUTH', token=str) = None,
):
	if not fcm_auth:
		fcm_auth = Registry.var('fcm')

	push_service = FCMNotification(api_key=fcm_auth['token'])
	push_service.notify_single_device(
		registration_id=registration_id,
		message_title=message_title,
		message_body=message_body,
		data_message=data_message,
	)


config = PACKAGE_CONFIG(
	api_level='1.0',
	version='1.0.0',
	gateways={'fcm': fcm_gateway},
	vars_types={'fcm': ATTR.TYPED_DICT(dict={'token': ATTR.STR()})},
)
