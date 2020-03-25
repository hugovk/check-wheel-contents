import pytest
from   check_wheel_contents.checker  import WheelChecker
from   check_wheel_contents.checks   import Check, FailedCheck
from   check_wheel_contents.contents import WheelContents

@pytest.mark.parametrize('rows,failures', [
    (
        [
            [
                'foo-1.0.dist-info/METADATA',
                'sha256=NVefY26xjCmYCQCnZaKUTNc5WaqZHDKxVde8l72cVOk',
                '950',
            ],
            [
                'foo.py',
                'sha256=UxbST6sF1RzAkvG8kCt15x13QBsB5FPeLnRJ4wHMqps',
                '1003',
            ],
        ],
        [],
    ),

    (
        [
            [
                'foo-1.0.dist-info/METADATA',
                'sha256=NVefY26xjCmYCQCnZaKUTNc5WaqZHDKxVde8l72cVOk',
                '950',
            ],
            [
                'foo.py',
                'sha256=UxbST6sF1RzAkvG8kCt15x13QBsB5FPeLnRJ4wHMqps',
                '1003',
            ],
            [
                'foo.pyc',
                'sha256=ZjTs9Wx4pXxwT5mNZJ8WoAt-9zeO9iaxYhNFES7BrIY',
                '1040',
            ],
        ],
        [FailedCheck(Check.W001, ['foo.pyc'])],
    ),

    (
        [
            [
                'foo-1.0.dist-info/METADATA',
                'sha256=NVefY26xjCmYCQCnZaKUTNc5WaqZHDKxVde8l72cVOk',
                '950',
            ],
            [
                'foo.py',
                'sha256=UxbST6sF1RzAkvG8kCt15x13QBsB5FPeLnRJ4wHMqps',
                '1003',
            ],
            [
                'foo.pyo',
                'sha256=ZjTs9Wx4pXxwT5mNZJ8WoAt-9zeO9iaxYhNFES7BrIY',
                '1040',
            ],
        ],
        [FailedCheck(Check.W001, ['foo.pyo'])],
    ),

    (
        [
            [
                'foo-1.0.dist-info/METADATA',
                'sha256=NVefY26xjCmYCQCnZaKUTNc5WaqZHDKxVde8l72cVOk',
                '950',
            ],
            [
                'foo.py',
                'sha256=UxbST6sF1RzAkvG8kCt15x13QBsB5FPeLnRJ4wHMqps',
                '1003',
            ],
            [
                '__pycache__/foo.cpython-36.pyc',
                'sha256=ZjTs9Wx4pXxwT5mNZJ8WoAt-9zeO9iaxYhNFES7BrIY',
                '1040',
            ],
        ],
        [FailedCheck(Check.W001, ['__pycache__/foo.cpython-36.pyc'])],
    ),

    (
        [
            [
                'foo-1.0.dist-info/METADATA',
                'sha256=NVefY26xjCmYCQCnZaKUTNc5WaqZHDKxVde8l72cVOk',
                '950',
            ],
            [
                'foo.py',
                'sha256=UxbST6sF1RzAkvG8kCt15x13QBsB5FPeLnRJ4wHMqps',
                '1003',
            ],
            [
                '__pycache__/foo.cpython-36.opt-1.pyc',
                'sha256=ZjTs9Wx4pXxwT5mNZJ8WoAt-9zeO9iaxYhNFES7BrIY',
                '1040',
            ],
        ],
        [FailedCheck(Check.W001, ['__pycache__/foo.cpython-36.opt-1.pyc'])],
    ),

    (
        [
            [
                'foo-1.0.dist-info/METADATA',
                'sha256=NVefY26xjCmYCQCnZaKUTNc5WaqZHDKxVde8l72cVOk',
                '950',
            ],
            [
                'foo/__init__.py',
                'sha256=f6qW0sceqJJFaqOMuDCf8aLvlAGGSAqMUv6_5fmEqnU',
                '986',
            ],
            [
                'foo/bar.py',
                'sha256=13nkC_buM-u8_X465GXhWtLBXiiwxDyKwzPXHcHfGZ8',
                '1002',
            ],
            [
                'foo/__pycache__/__init__.cpython-36.pyc',
                'sha256=rHJbQE_4bKobwU3-bMSwroezXhWdAD_WGeVskhfmJfs',
                '1031',
            ],
            [
                'foo/__pycache__/bar.cpython-36.pyc',
                'sha256=_Bwzc6pX7GqAcXhljEKl0rhdf_ddb-X5vRfU0MztA4s',
                '1075',
            ],
            [
                'foo/subfoo/__init__.py',
                'sha256=Nklhzg65B016HWZdCkOOV8Wj3HkSmIUPnyeTmXXSmyo',
                '1058',
            ],
            [
                'foo/subfoo/__pycache__/__init__.cpython-36.pyc',
                'sha256=ZcfO0RZv7YeeyIaZSMQAVHJjsjRsiwj85m3zqKZX4Kg',
                '1010',
            ],
        ],
        [FailedCheck(
            Check.W001,
            [
                'foo/__pycache__/__init__.cpython-36.pyc',
                'foo/__pycache__/bar.cpython-36.pyc',
                'foo/subfoo/__pycache__/__init__.cpython-36.pyc',
            ],
        )],
    ),

    (
        [
            [
                'foo-1.0.dist-info/METADATA',
                'sha256=NVefY26xjCmYCQCnZaKUTNc5WaqZHDKxVde8l72cVOk',
                '950',
            ],
            [
                'foo.py',
                'sha256=UxbST6sF1RzAkvG8kCt15x13QBsB5FPeLnRJ4wHMqps',
                '1003',
            ],
            [
                'foo-1.0.dist-info/how-did-this-get-here.pyc',
                'sha256=iKmjZrSZ3et2vMFF_Wxmtv6mjmci6Gm8TyvAeu9KT7s',
                '988',
            ],
        ],
        [FailedCheck(Check.W001, ['foo-1.0.dist-info/how-did-this-get-here.pyc',])],
    ),

    (
        [
            [
                'foo-1.0.dist-info/METADATA',
                'sha256=NVefY26xjCmYCQCnZaKUTNc5WaqZHDKxVde8l72cVOk',
                '950',
            ],
            [
                'foo-1.0.data/platlib/foo.py',
                'sha256=9LpEj5Zw0laBNRM8ENYpfQmkjxRIy8tKOObUEpNy6NA',
                '1040',
            ],
            [
                'foo-1.0.data/platlib/__pycache__/foo.cpython-36.pyc',
                'sha256=6_TatpFL-LF3q8NAOEPPGuZVXrq0epNoKRyk_HVRoiM',
                '980',
            ],
        ],
        [FailedCheck(Check.W001, ['foo-1.0.data/platlib/__pycache__/foo.cpython-36.pyc'])],
    ),

    (
        [
            [
                'foo-1.0.dist-info/METADATA',
                'sha256=NVefY26xjCmYCQCnZaKUTNc5WaqZHDKxVde8l72cVOk',
                '950',
            ],
            [
                'foo-1.0.data/other/foo.py',
                'sha256=9LpEj5Zw0laBNRM8ENYpfQmkjxRIy8tKOObUEpNy6NA',
                '1040',
            ],
            [
                'foo-1.0.data/other/__pycache__/foo.cpython-36.pyc',
                'sha256=6_TatpFL-LF3q8NAOEPPGuZVXrq0epNoKRyk_HVRoiM',
                '980',
            ],
        ],
        [FailedCheck(Check.W001, ['foo-1.0.data/other/__pycache__/foo.cpython-36.pyc'])],
    ),
])
def test_check_W001(rows, failures):
    whlcon = WheelContents(
        dist_info_dir='foo-1.0.dist-info',
        data_dir='foo-1.0.data',
        root_is_purelib=True,
    )
    whlcon.add_record_rows(rows)
    whlcon.validate_tree()
    checker = WheelChecker()
    assert checker.check_W001(whlcon) == failures
