# pyrefly: ignore [missing-import]
import pytest
from datetime import datetime, timedelta
from src.aaptics_engine import AapticsEngine

@pytest.fixture
def engine():
    return AapticsEngine()

# === ТЕСТИ ДЛЯ МЕТОДУ create_voice_dna ===

def test_create_voice_dna_success_three_samples(engine):
    # Arrange
    samples = ["Текст приклад один два", "Другий довгий текст автора", "Третій зразок стилю написання"]
    # Act
    result = engine.create_voice_dna(samples)
    # Assert
    assert result == "VoiceDNA_Profile_Based_On_3_Samples"

def test_create_voice_dna_success_four_samples(engine):
    # Arrange
    samples = ["Текст приклад один два", "Другий довгий текст автора", "Третій зразок стилю написання", "Четвертий фінальний текст"]
    # Act
    result = engine.create_voice_dna(samples)
    # Assert
    assert result == "VoiceDNA_Profile_Based_On_4_Samples"

def test_create_voice_dna_too_few_samples(engine):
    # Arrange
    samples = ["Короткий текст один", "Другий текст автора"]
    # Act & Assert
    with pytest.raises(ValueError, match="Must provide exactly 3 or 4 sample texts"):
        engine.create_voice_dna(samples)

def test_create_voice_dna_too_many_samples(engine):
    # Arrange
    samples = ["Текст один довгий", "Текст два довгий", "Текст три довгий", "Текст чотири довгий", "Текст п'ять довгий"]
    # Act & Assert
    with pytest.raises(ValueError, match="Must provide exactly 3 or 4 sample texts"):
        engine.create_voice_dna(samples)

def test_create_voice_dna_invalid_text_length(engine):
    # Arrange
    samples = ["Валідний текст один", "Валідний текст два", "Шорт"]
    # Act & Assert
    with pytest.raises(ValueError, match="Each text must be at least 10 characters long"):
        engine.create_voice_dna(samples)


# === ТЕСТИ ДЛЯ МЕТОДУ generate_post_content ===

def test_generate_post_success(engine):
    # Arrange
    idea = "Новий пост про тренди ШІ в 2026 році"
    profile = "VoiceDNA_Profile_Based_On_3_Samples"
    # Act
    post = engine.generate_post_content(idea, profile)
    # Assert
    assert "using VoiceDNA_Profile_Based_On_3_Samples" in post
    assert "Новий пост про тренди ШІ" in post

def test_generate_post_idea_too_short(engine):
    # Arrange
    idea = "ШІ"  # 2 символи
    profile = "VoiceDNA_Profile_Based_On_3_Samples"
    # Act & Assert
    with pytest.raises(ValueError, match="Idea must be at least 5 characters long"):
        engine.generate_post_content(idea, profile)

def test_generate_post_idea_too_long(engine):
    # Arrange
    idea = "A" * 501
    profile = "VoiceDNA_Profile_Based_On_3_Samples"
    # Act & Assert
    with pytest.raises(ValueError, match="Idea cannot exceed 500 characters"):
        engine.generate_post_content(idea, profile)

def test_generate_post_invalid_profile(engine):
    # Arrange
    idea = "Валідна ідея для публікації"
    profile = "Invalid_Mock_Profile"
    # Act & Assert
    with pytest.raises(ValueError, match="Invalid or missing Voice DNA profile"):
        engine.generate_post_content(idea, profile)


# === ТЕСТИ ДЛЯ МЕТОДУ schedule_publication ===

def test_schedule_success(engine):
    # Arrange
    content = "Гарний та структурований контент для LinkedIn"
    future_date = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d %H:%M")
    # Act
    result = engine.schedule_publication(content, future_date)
    # Assert
    assert result is True

def test_schedule_past_date(engine):
    # Arrange
    content = "Контент для LinkedIn"
    past_date = "2020-01-01 12:00"
    # Act & Assert
    with pytest.raises(ValueError, match="Scheduled date must be in the future"):
        engine.schedule_publication(content, past_date)

def test_schedule_invalid_date_format(engine):
    # Arrange
    content = "Контент для LinkedIn"
    bad_date = "31-12-2026 12:00"
    # Act & Assert
    with pytest.raises(ValueError, match="Invalid date format. Use YYYY-MM-DD HH:MM"):
        engine.schedule_publication(content, bad_date)

def test_schedule_content_too_long(engine):
    # Arrange
    content = "X" * 3001
    future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    # Act & Assert
    with pytest.raises(ValueError, match="Post content cannot exceed 3000 characters"):
        engine.schedule_publication(content, future_date)