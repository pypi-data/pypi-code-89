"""
HTTP codes
See RFC 2616 - https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
And RFC 6585 - https://tools.ietf.org/html/rfc6585
And RFC 4918 - https://tools.ietf.org/html/rfc4918
And RFC 8470 - https://tools.ietf.org/html/rfc8470
"""
HTTP_100_CONTINUE = 100
HTTP_101_SWITCHING_PROTOCOLS = 101
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_202_ACCEPTED = 202
HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203
HTTP_204_NO_CONTENT = 204
HTTP_205_RESET_CONTENT = 205
HTTP_206_PARTIAL_CONTENT = 206
HTTP_207_MULTI_STATUS = 207
HTTP_300_MULTIPLE_CHOICES = 300
HTTP_301_MOVED_PERMANENTLY = 301
HTTP_302_FOUND = 302
HTTP_303_SEE_OTHER = 303
HTTP_304_NOT_MODIFIED = 304
HTTP_305_USE_PROXY = 305
HTTP_306_RESERVED = 306
HTTP_307_TEMPORARY_REDIRECT = 307
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_402_PAYMENT_REQUIRED = 402
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
HTTP_405_METHOD_NOT_ALLOWED = 405
HTTP_406_NOT_ACCEPTABLE = 406
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407
HTTP_408_REQUEST_TIMEOUT = 408
HTTP_409_CONFLICT = 409
HTTP_410_GONE = 410
HTTP_411_LENGTH_REQUIRED = 411
HTTP_412_PRECONDITION_FAILED = 412
HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413
HTTP_414_REQUEST_URI_TOO_LONG = 414
HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416
HTTP_417_EXPECTATION_FAILED = 417
HTTP_422_UNPROCESSABLE_ENTITY = 422
HTTP_423_LOCKED = 423
HTTP_424_FAILED_DEPENDENCY = 424
HTTP_425_TOO_EARLY = 425
HTTP_428_PRECONDITION_REQUIRED = 428
HTTP_429_TOO_MANY_REQUESTS = 429
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451
HTTP_500_INTERNAL_SERVER_ERROR = 500
HTTP_501_NOT_IMPLEMENTED = 501
HTTP_502_BAD_GATEWAY = 502
HTTP_503_SERVICE_UNAVAILABLE = 503
HTTP_504_GATEWAY_TIMEOUT = 504
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505
HTTP_507_INSUFFICIENT_STORAGE = 507
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511


"""
WebSocket codes
https://www.iana.org/assignments/websocket/websocket.xml#close-code-number
https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent
"""
WS_1000_NORMAL_CLOSURE = 1000
WS_1001_GOING_AWAY = 1001
WS_1002_PROTOCOL_ERROR = 1002
WS_1003_UNSUPPORTED_DATA = 1003
WS_1004_NO_STATUS_RCVD = 1004
WS_1005_ABNORMAL_CLOSURE = 1005
WS_1007_INVALID_FRAME_PAYLOAD_DATA = 1007
WS_1008_POLICY_VIOLATION = 1008
WS_1009_MESSAGE_TOO_BIG = 1009
WS_1010_MANDATORY_EXT = 1010
WS_1011_INTERNAL_ERROR = 1011
WS_1012_SERVICE_RESTART = 1012
WS_1013_TRY_AGAIN_LATER = 1013
WS_1014_BAD_GATEWAY = 1014
WS_1015_TLS_HANDSHAKE = 1015
