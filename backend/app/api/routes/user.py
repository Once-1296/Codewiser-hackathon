"""User-related API routes for logging cognitive state."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from backend.app.api.deps import get_energy_service
from backend.app.schemas.common import APIResponse
from backend.app.schemas.user import EnergyPredictionResponse, UserState
from backend.app.services.energy_service import EnergyService

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/logs", response_model=APIResponse[EnergyPredictionResponse])
def log_user_state(
    user_state: UserState,
    energy_service: EnergyService = Depends(get_energy_service),
) -> APIResponse[EnergyPredictionResponse]:
    """Accept a user state snapshot and return an energy estimate."""

    prediction = energy_service.predict_energy(user_state)
    return APIResponse(message="User state logged", data=prediction)

