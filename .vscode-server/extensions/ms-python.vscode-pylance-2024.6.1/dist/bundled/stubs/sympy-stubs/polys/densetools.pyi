from typing import Any

def dup_integrate(f, m, K): ...
def dmp_integrate(f, m, u, K) -> list[Any] | list[list[list[Any]]]: ...
def dmp_integrate_in(f, m, j, u, K) -> list[Any] | list[list[list[Any]]] | list[list[Any]]: ...
def dup_diff(f, m, K) -> list[Any]: ...
def dmp_diff(f, m, u, K) -> list[Any] | list[list[Any]]: ...
def dmp_diff_in(f, m, j, u, K) -> list[Any] | list[list[Any]]: ...
def dup_eval(f, a, K): ...
def dmp_eval(f, a, u, K) -> list[list[Any]]: ...
def dmp_eval_in(f, a, j, u, K) -> list[list[Any]]: ...
def dmp_eval_tail(f, A, u, K) -> list[list[Any]] | list[Any]: ...
def dmp_diff_eval_in(f, m, a, j, u, K) -> list[list[Any]]: ...
def dup_trunc(f, p, K): ...
def dmp_trunc(f, p, u, K) -> list[list[Any]]: ...
def dmp_ground_trunc(f, p, u, K) -> list[list[Any]]: ...
def dup_monic(f, K) -> list[Any]: ...
def dmp_ground_monic(f, u, K) -> list[Any]: ...
def dup_content(f, K): ...
def dmp_ground_content(f, u, K): ...
def dup_primitive(f, K) -> tuple[Any, Any] | tuple[Any, Any | list[Any]]: ...
def dmp_ground_primitive(f, u, K) -> tuple[Any, Any] | tuple[Any, Any | list[Any]]: ...
def dup_extract(f, g, K) -> tuple[Any, Any | list[Any], Any | list[Any]]: ...
def dmp_ground_extract(f, g, u, K) -> tuple[Any, Any | list[Any], Any | list[Any]]: ...
def dup_real_imag(
    f, K
) -> tuple[list[list[Any]], list[list[Any]]] | tuple[list[list[Any]] | Any | list[Any], list[list[Any]] | Any | list[Any]]: ...
def dup_mirror(f, K) -> list[Any]: ...
def dup_scale(f, a, K) -> list[Any]: ...
def dup_shift(f, a, K) -> list[Any]: ...
def dup_transform(f, p, q, K) -> list[Any]: ...
def dup_compose(f, g, K) -> list[Any]: ...
def dmp_compose(f, g, u, K) -> list[Any] | list[list[Any]]: ...
def dup_decompose(f, K) -> list[Any | list[Any]]: ...
def dmp_lift(f, u, K) -> list[list[Any]]: ...
def dup_sign_variations(f, K) -> int: ...
def dup_clear_denoms(f, K0, K1=..., convert=...) -> tuple[Any, list[Any] | Any] | tuple[Any, Any]: ...
def dmp_clear_denoms(
    f, u, K0, K1=..., convert=...
) -> tuple[Any, list[Any] | Any] | tuple[Any, Any] | tuple[Any, Any | list[list[Any]]]: ...
def dup_revert(f, n, K) -> list[Any]: ...
def dmp_revert(f, g, u, K) -> list[Any]: ...
