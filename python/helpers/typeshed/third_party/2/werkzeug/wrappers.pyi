# Stubs for werkzeug.wrappers (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class BaseRequest:
    charset = ...  # type: Any
    encoding_errors = ...  # type: Any
    max_content_length = ...  # type: Any
    max_form_memory_size = ...  # type: Any
    parameter_storage_class = ...  # type: Any
    list_storage_class = ...  # type: Any
    dict_storage_class = ...  # type: Any
    form_data_parser_class = ...  # type: Any
    trusted_hosts = ...  # type: Any
    disable_data_descriptor = ...  # type: Any
    environ = ...  # type: Any
    shallow = ...  # type: Any
    def __init__(self, environ, populate_request=True, shallow=False): ...
    @property
    def url_charset(self): ...
    @classmethod
    def from_values(cls, *args, **kwargs): ...
    @classmethod
    def application(cls, f): ...
    @property
    def want_form_data_parsed(self): ...
    def make_form_data_parser(self): ...
    def close(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, tb): ...
    def stream(self): ...
    input_stream = ...  # type: Any
    def args(self): ...
    def data(self): ...
    def get_data(self, cache=True, as_text=False, parse_form_data=False): ...
    def form(self): ...
    def values(self): ...
    def files(self): ...
    def cookies(self): ...
    def headers(self): ...
    def path(self): ...
    def full_path(self): ...
    def script_root(self): ...
    def url(self): ...
    def base_url(self): ...
    def url_root(self): ...
    def host_url(self): ...
    def host(self): ...
    query_string = ...  # type: Any
    method = ...  # type: Any
    def access_route(self): ...
    @property
    def remote_addr(self): ...
    remote_user = ...  # type: Any
    scheme = ...  # type: Any
    is_xhr = ...  # type: Any
    is_secure = ...  # type: Any
    is_multithread = ...  # type: Any
    is_multiprocess = ...  # type: Any
    is_run_once = ...  # type: Any

class BaseResponse:
    charset = ...  # type: Any
    default_status = ...  # type: Any
    default_mimetype = ...  # type: Any
    implicit_sequence_conversion = ...  # type: Any
    autocorrect_location_header = ...  # type: Any
    automatically_set_content_length = ...  # type: Any
    headers = ...  # type: Any
    status_code = ...  # type: Any
    status = ...  # type: Any
    direct_passthrough = ...  # type: Any
    response = ...  # type: Any
    def __init__(self, response=None, status=None, headers=None, mimetype=None, content_type=None, direct_passthrough=False): ...
    def call_on_close(self, func): ...
    @classmethod
    def force_type(cls, response, environ=None): ...
    @classmethod
    def from_app(cls, app, environ, buffered=False): ...
    def get_data(self, as_text=False): ...
    def set_data(self, value): ...
    data = ...  # type: Any
    def calculate_content_length(self): ...
    def make_sequence(self): ...
    def iter_encoded(self): ...
    def set_cookie(self, key, value='', max_age=None, expires=None, path='', domain=None, secure=False, httponly=False): ...
    def delete_cookie(self, key, path='', domain=None): ...
    @property
    def is_streamed(self): ...
    @property
    def is_sequence(self): ...
    def close(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, tb): ...
    def freeze(self): ...
    def get_wsgi_headers(self, environ): ...
    def get_app_iter(self, environ): ...
    def get_wsgi_response(self, environ): ...
    def __call__(self, environ, start_response): ...

class AcceptMixin:
    def accept_mimetypes(self): ...
    def accept_charsets(self): ...
    def accept_encodings(self): ...
    def accept_languages(self): ...

class ETagRequestMixin:
    def cache_control(self): ...
    def if_match(self): ...
    def if_none_match(self): ...
    def if_modified_since(self): ...
    def if_unmodified_since(self): ...
    def if_range(self): ...
    def range(self): ...

class UserAgentMixin:
    def user_agent(self): ...

class AuthorizationMixin:
    def authorization(self): ...

class StreamOnlyMixin:
    disable_data_descriptor = ...  # type: Any
    want_form_data_parsed = ...  # type: Any

class ETagResponseMixin:
    @property
    def cache_control(self): ...
    status_code = ...  # type: Any
    def make_conditional(self, request_or_environ, accept_ranges=False, complete_length=None): ...
    def add_etag(self, overwrite=False, weak=False): ...
    def set_etag(self, etag, weak=False): ...
    def get_etag(self): ...
    def freeze(self, no_etag=False): ...
    accept_ranges = ...  # type: Any
    content_range = ...  # type: Any

class ResponseStream:
    mode = ...  # type: Any
    response = ...  # type: Any
    closed = ...  # type: Any
    def __init__(self, response): ...
    def write(self, value): ...
    def writelines(self, seq): ...
    def close(self): ...
    def flush(self): ...
    def isatty(self): ...
    @property
    def encoding(self): ...

class ResponseStreamMixin:
    def stream(self): ...

class CommonRequestDescriptorsMixin:
    content_type = ...  # type: Any
    def content_length(self): ...
    content_encoding = ...  # type: Any
    content_md5 = ...  # type: Any
    referrer = ...  # type: Any
    date = ...  # type: Any
    max_forwards = ...  # type: Any
    @property
    def mimetype(self): ...
    @property
    def mimetype_params(self): ...
    def pragma(self): ...

class CommonResponseDescriptorsMixin:
    mimetype = ...  # type: Any
    mimetype_params = ...  # type: Any
    location = ...  # type: Any
    age = ...  # type: Any
    content_type = ...  # type: Any
    content_length = ...  # type: Any
    content_location = ...  # type: Any
    content_encoding = ...  # type: Any
    content_md5 = ...  # type: Any
    date = ...  # type: Any
    expires = ...  # type: Any
    last_modified = ...  # type: Any
    retry_after = ...  # type: Any
    vary = ...  # type: Any
    content_language = ...  # type: Any
    allow = ...  # type: Any

class WWWAuthenticateMixin:
    @property
    def www_authenticate(self): ...

class Request(BaseRequest, AcceptMixin, ETagRequestMixin, UserAgentMixin, AuthorizationMixin, CommonRequestDescriptorsMixin): ...
class PlainRequest(StreamOnlyMixin, Request): ...
class Response(ETagResponseMixin, BaseResponse, ResponseStreamMixin, CommonResponseDescriptorsMixin, WWWAuthenticateMixin): ...   # FIXME: This is invalid but works around https://github.com/pallets/werkzeug/issues/1052
