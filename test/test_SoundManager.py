import pytest
from unittest.mock import patch, MagicMock
from BackEnd.SoundManager import SoundManager

@pytest.fixture(autouse=True)
def mock_pygame_mixer():
    """Фікстура для мокування pygame.mixer. Використовується для заміни реального pygame.mixer
    під час тестів, щоб запобігти викликам реальних функцій міксера звуків.
    """
    with patch('pygame.mixer.init'), \
            patch('pygame.mixer.Sound'), \
            patch('pygame.mixer.Channel'):
        yield

@pytest.fixture(autouse=True)
def init_pygame():
    """Фікстура для ініціалізації та завершення роботи pygame для кожного тесту.
    Використовується для мокування викликів pygame.init() і pygame.quit().
    """
    with patch('pygame.init'), \
            patch('pygame.quit'):
        yield

def test_load_sounds():
    """Тест перевіряє завантаження звуків у менеджер звуків.
    Переконуємося, що всі необхідні звуки завантажуються в список менеджера.
    """
    with patch('pygame.mixer.Sound') as mock_sound:
        # Arrange: підготовка. Мокування pygame.mixer.Sound, щоб не викликати реальні звукові файли.
        mock_sound.return_value = MagicMock()  # Мокуємо екземпляр звуку.
        sound_manager = SoundManager()  # Створюємо об'єкт менеджера звуків.

        # Act: викликаємо метод завантаження звуків.
        sound_manager.load_sounds()

        # Assert: перевірка результатів.
        # Переконуємося, що в списку звуків є всі необхідні елементи.
        assert len(sound_manager.sounds) == 4  # Перевіряємо, що всього 4 звуки.
        assert all(sound in sound_manager.sounds for sound in ['monster', 'plate', 'bird', 'laser'])  # Перевіряємо кожен звук.
        assert mock_sound.call_count == 8  # Перевіряємо, що викликано 8 разів метод pygame.mixer.Sound (по 2 для кожного звуку).

def test_play_sound():
    """Тест перевіряє відтворення звуку за запитом.
    Переконуємося, що звук відтворюється правильно, коли його ім'я передається в метод play_sound.
    """
    with patch('pygame.mixer.Sound') as mock_sound:
        # Arrange: підготовка. Мокуємо Sound для тестування.
        mock_sound_instance = MagicMock()  # Мокування самого звуку.
        mock_sound.return_value = mock_sound_instance  # Повертаємо мокований екземпляр.
        sound_manager = SoundManager()  # Створюємо об'єкт менеджера звуків.
        sound_manager.load_sounds()  # Завантажуємо звуки в менеджер.

        # Act: викликаємо метод відтворення звуку для звуку "monster".
        sound_manager.play_sound('monster')

        # Assert: перевіряємо, що метод play на мокованому звуці був викликаний.
        mock_sound_instance.play.assert_called_once()  # Перевіряємо, що play був викликаний рівно один раз.

def test_play_nonexistent_sound():
    """Тест перевіряє, що метод play не викликається для неіснуючого звуку.
    Переконуємося, що метод play не викликається для звуку, якого немає в списку.
    """
    with patch('pygame.mixer.Sound') as mock_sound:
        # Arrange: підготовка.
        sound_manager = SoundManager()  # Створюємо об'єкт менеджера звуків.
        sound_manager.load_sounds()  # Завантажуємо доступні звуки.

        # Act: намагаємося відтворити неіснуючий звук.
        sound_manager.play_sound('nonexistent')

        # Assert: перевіряємо, що метод play не був викликаний для цього звуку.
        mock_sound.return_value.play.assert_not_called()  # Перевіряємо, що play не був викликаний.

if __name__ == '__main__':
    pytest.main(['-v'])  # Запускаємо тести з детальним виведенням.
