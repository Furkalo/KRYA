import pytest
import pygame

import sys
import os

from BackEnd.Gun import Gun

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'BackEnd')))


@pytest.fixture
def setup_gun():
    """Фікстура для налаштування об'єкта Gun та супутніх властивостей"""
    pygame.init()
    width = 800
    height = 600
    gun_images = [pygame.Surface((50, 50)) for _ in range(3)]  # Мокування зображень
    gun = Gun(width, height, gun_images)
    return gun, width, height

def test_calculate_rotation(setup_gun):
    """Тестування правильного обчислення кута обертання рушниці"""
    gun, width, height = setup_gun
    mouse_pos = (width // 2 + 1, height - 250)  # Легке зміщення вправо, щоб уникнути ділення на 0
    angle = gun.calculate_rotation(mouse_pos)
    assert -90 <= angle <= 90, f"Очікуваний кут між -90 і 90, але отримано {angle}"

def test_lasers_colors(setup_gun):
    """Тестування правильності списку кольорів лазерів"""
    gun, _, _ = setup_gun
    assert gun.lasers == ['red', 'purple', 'green'], f"Очікувані кольори лазерів ['red', 'purple', 'green'], але отримано {gun.lasers}"

def test_draw(setup_gun):
    """Тестування, що метод draw не викликає помилок при малюванні"""
    gun, width, height = setup_gun
    screen = pygame.Surface((width, height))
    mouse_pos = (width // 2, height // 2)
    try:
        gun.draw(screen, level=1, mouse_pos=mouse_pos)
    except Exception as e:
        pytest.fail(f"Метод draw викликав помилку: {e}")


if __name__ == "__main__":
    pytest.main()
    print(sys.path)
