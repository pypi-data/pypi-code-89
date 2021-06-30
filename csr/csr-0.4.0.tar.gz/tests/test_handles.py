"""
Tests for creating kernel handles.
"""

from csr.test_utils import csrs

from hypothesis import given


@given(csrs())
def test_make_handle(kernel, csr):
    h = kernel.to_handle(csr.R)
    try:
        assert h is not None
        c2 = kernel.from_handle(h)
        assert c2.nrows == csr.nrows
        assert c2.ncols == csr.ncols
        assert c2.nnz == csr.nnz
    finally:
        kernel.release_handle(h)
