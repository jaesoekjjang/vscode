from _typeshed import Incomplete
from collections.abc import Callable
from logging import Logger
from typing import Any, Generic, NoReturn, TypeVar
from typing_extensions import Self, TypeAlias

from ..engine.interfaces import Connectable
from ..engine.url import URL
from .config import Config, _ConfigProtocol

_Unused: TypeAlias = object
_S = TypeVar("_S", bound=str)
_U = TypeVar("_U", bound=URL)
_F = TypeVar("_F", bound=Callable[..., str | URL | None])

log: Logger
FOLLOWER_IDENT: Incomplete | None

def create_follower_db(follower_ident) -> None: ...
def setup_config(db_url, options, file_config, follower_ident) -> Config: ...
def drop_follower_db(follower_ident) -> None: ...
def generate_db_urls(db_urls, extra_drivers) -> None: ...
def drop_all_schema_objects(cfg, eng) -> None: ...
def reap_dbs(idents_file) -> None: ...

class register(Generic[_F]):
    fns: dict[str, _F]
    @classmethod
    def init(cls, fn: _F) -> Self: ...
    def for_db(self, *dbnames: str) -> Callable[[_F], Self]: ...
    # Impossible to specify the args from the generic Callable in the current type system
    def __call__(self, cfg: str | URL | _ConfigProtocol, *arg: Any) -> str | URL | None: ...  # AnyOf[str | URL | None]

@register.init
def generate_driver_url(url: _U, driver: str, query_str: str) -> _U | None: ...
@register.init
def drop_all_schema_objects_pre_tables(cfg: _Unused, eng: _Unused) -> None: ...
@register.init
def drop_all_schema_objects_post_tables(cfg: _Unused, eng: _Unused) -> None: ...
@register.init
def create_db(cfg: _Unused, eng: Connectable, ident: _Unused) -> NoReturn: ...
@register.init
def drop_db(cfg: _Unused, eng: Connectable, ident: _Unused) -> NoReturn: ...
@register.init
def update_db_opts(db_url: _Unused, db_opts: _Unused) -> None: ...
@register.init
def post_configure_engine(url: _Unused, engine: _Unused, follower_ident: _Unused) -> None: ...
@register.init
def follower_url_from_main(url: _U, ident: str) -> _U: ...
@register.init
def configure_follower(cfg: _Unused, ident: _Unused) -> None: ...
@register.init
def run_reap_dbs(url: _Unused, ident: _Unused) -> None: ...
@register.init
def temp_table_keyword_args(cfg: _Unused, eng: Connectable) -> NoReturn: ...
@register.init
def prepare_for_drop_tables(config: _Unused, connection: _Unused) -> None: ...
@register.init
def stop_test_class_outside_fixtures(config: _Unused, db: _Unused, testcls: _Unused) -> None: ...
@register.init  # type: ignore[type-var]  # False-positive, _S is bound to str
def get_temp_table_name(cfg: _Unused, eng: _Unused, base_name: _S) -> _S: ...
@register.init
def set_default_schema_on_connection(cfg: _ConfigProtocol, dbapi_connection: _Unused, schema_name: _Unused) -> NoReturn: ...
