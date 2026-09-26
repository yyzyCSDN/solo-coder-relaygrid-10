import pytest

from relaygrid.ev.charging import allocate_ev
from relaygrid.interchange.tie_capacity import transferable_kw
from relaygrid.storage.dispatch import StorageState, dispatch


def test_flexibility_dispatch_preserves_energy_and_physical_limits():
    actual, state = dispatch(
        StorageState(energy_kwh=80.0, capacity_kwh=100.0, min_soc=0.1),
        requested_kw=50.0,
        duration_h=1.0,
        discharge_eff=0.8,
    )
    assert actual == pytest.approx(50.0)
    assert state.energy_kwh == pytest.approx(17.5)

    allocation = allocate_ev(
        [("bad", -5.0, 1.0), ("good", 20.0, 2.0)],
        feeder_headroom_kw=20.0,
    )
    assert allocation == {"bad": 0.0, "good": 20.0}

    with pytest.raises(ValueError, match="power factor"):
        transferable_kw(100.0, 12.47, 1.2, 1000.0, 1000.0)
