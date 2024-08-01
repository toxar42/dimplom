import pytest
from dip.libs.add.ES import *

@pytest.fixture
def car_expert_system():
    return CARS()

@pytest.mark.parametrize(
    "facts, expected_car",
    [
        ([Fact('комфорт'), Fact('3000000-4000000'), Fact('универсал'),
         Fact('off-road приключения'), Fact('полный')], 'Volvo V90 2020'),
    ]
)
def test_identification_car(car_expert_system, facts, expected_car, monkeypatch):
    # Тестирует идентификацию автомобиля на основе предоставленных фактов.
    monkeypatch.setattr('dip.libs.add.ES', '')# Патчим глобальную переменную
    car_expert_system.reset()
    car_expert_system.factz(facts)
    car_expert_system.run()
    identify(facts)  # Вызываем функцию identify для записи результата в файл
    with open("identified_car.json", "r") as f:
        result = json.load(f)
    assert result["car"] == expected_car




