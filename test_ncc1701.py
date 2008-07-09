# -*- coding: UTF-8 -*-

import ncc1701


def test_phasers():
    p=ncc1701.Phaser()
    assert hasattr(p,"lock_target")
    assert hasattr(p,"fire")
    