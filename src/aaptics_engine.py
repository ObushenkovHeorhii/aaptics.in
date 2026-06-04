import re
from datetime import datetime

class AapticsEngine:
    def __init__(self):
        self.voice_dna_profile = None

    def create_voice_dna(self, sample_texts: list) -> str:
        """
        Метод 1: Навчання моделі стилю автора. 
        Очікує на вхід список, який містить рівно від 3 до 4 текстів.
        Кажний текст повинен бути рядком довжиною не менше 10 символів.
        """
        if not isinstance(sample_texts, list):
            raise TypeError("Sample texts must be a list")
        
        # Перевірка кількості елементів (Границі: 3 та 4 тексти)
        if len(sample_texts) < 3 or len(sample_texts) > 4:
            raise ValueError("Must provide exactly 3 or 4 sample texts")
        
        # Валідація вмісту кожного тексту
        for text in sample_texts:
            if not isinstance(text, str):
                raise TypeError("Each sample text must be a string")
            if len(text.strip()) < 10:
                raise ValueError("Each text must be at least 10 characters long")
        
        # Симуляція формування унікального профілю
        self.voice_dna_profile = f"VoiceDNA_Profile_Based_On_{len(sample_texts)}_Samples"
        return self.voice_dna_profile

    def generate_post_content(self, idea: str, dna_profile: str) -> str:
        """
        Метод 2: Генерація тексту на основі короткої ідеї та ДНК-профілю.
        Довжина ідеї має бути в межах від 5 до 500 символів. Profile має бути валідним.
        """
        if not idea or not isinstance(idea, str):
            raise TypeError("Idea must be a non-empty string")
        
        if len(idea.strip()) < 5:
            raise ValueError("Idea must be at least 5 characters long")
            
        if len(idea) > 500:
            raise ValueError("Idea cannot exceed 500 characters")
            
        if not dna_profile or not isinstance(dna_profile, str) or "VoiceDNA" not in dna_profile:
            raise ValueError("Invalid or missing Voice DNA profile")
        
        # Імітація генерації тексту (максимум 3000 символів за вимогами)
        generated_text = f"[Generated LinkedIn Post using {dna_profile}]: {idea.strip()}"
        return generated_text[:3000]

    def schedule_publication(self, content: str, date_str: str) -> bool:
        """
        Метод 3: Валідація та планування відкладеної публікації.
        Текст не має бути порожнім і не може перевищувати 3000 символів.
        Дата має бути у форматі 'YYYY-MM-DD HH:MM' і вказувати на майбутнє.
        """
        if not content or len(content.strip()) == 0:
            raise ValueError("Post content cannot be empty")
            
        if len(content) > 3000:
            raise ValueError("Post content cannot exceed 3000 characters")
            
        # Валідація формату дати
        try:
            scheduled_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD HH:MM")
            
        # Дата має бути в майбутньому (симуляція відносно поточного часу виконання)
        if scheduled_date <= datetime.now():
            raise ValueError("Scheduled date must be in the future")
            
        return True