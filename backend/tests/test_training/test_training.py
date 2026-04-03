from backend.training.dataset_loader import (
    generate_energy_dataset,
    generate_task_dataset
)


def test_energy_dataset():
    df = generate_energy_dataset(100)

    assert not df.empty
    assert "energy_score" in df.columns


def test_task_dataset():
    df = generate_task_dataset(100)

    assert not df.empty
    assert "difficulty" in df.columns
    
def test_energy_range():
    df = generate_energy_dataset(100)

    assert df["energy_score"].between(0, 1).all()