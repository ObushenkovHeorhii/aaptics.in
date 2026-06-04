import re
from datetime import datetime

class AapticsEngine:
    # --- КОНСТАНТИ КЛАСУ (Рефакторинг: Replace Magic Number with Constant) ---
    MIN_SAMPLES = 3
    MAX_SAMPLES = 4
    MAX_POST_LENGTH = 3000
    MIN_IDEA_LENGTH = 5
    MAX_IDEA_LENGTH = 500
    DATE_FORMAT = "%Y-%m-%d %H:%M"

    def __init__(self):
        self.voice_dna_profile = None

    def create_voice_dna(self, sample_texts: list) -> str:
        """
        Метод 1: Навчання моделі стилю автора.
        Очікує список, який містить рівно 3 або 4 тексти.
        Кожен текст повинен бути рядком довжиною не менше 10 символів.
        """
        if not isinstance(sample_texts, list):
            raise TypeError("Sample texts must be a list")
        
        # Перевірка кількості елементів з використанням іменованих констант
        if len(sample_texts) < self.MIN_SAMPLES or len(sample_texts) > self.MAX_SAMPLES:
            raise ValueError(f"Must provide exactly {self.MIN_SAMPLES} or {self.MAX_SAMPLES} sample texts")
        
        # Валідація кожного окремого тексту
        for text in sample_texts:
            if not isinstance(text, str):
                raise TypeError("Each sample text must be a string")
            if len(text.strip()) < 10:
                raise ValueError("Each text must be at least 10 characters long")
        
        self.voice_dna_profile = f"VoiceDNA_Profile_Based_On_{len(sample_texts)}_Samples"
        return self.voice_dna_profile

    def _is_valid_profile(self, profile: str) -> bool:
        """
        Метод-хелпер для валідації профілю.
        (Рефакторинг: Extract Method та Simplify Conditional)
        """
        return bool(profile and isinstance(profile, str) and "VoiceDNA" in profile)

    def generate_post_content(self, idea: str, dna_profile: str) -> str:
        """
        Метод 2: Генерація тексту на основі короткої ідеї та ДНК-профілю.
        """
        if not idea or not isinstance(idea, str):
            raise TypeError("Idea must be a non-empty string")
        
        if len(idea.strip()) < self.MIN_IDEA_LENGTH:
            raise ValueError(f"Idea must be at least {self.MIN_IDEA_LENGTH} characters long")
            
        if len(idea) > self.MAX_IDEA_LENGTH:
            raise ValueError(f"Idea cannot exceed {self.MAX_IDEA_LENGTH} characters")
            
        # Використання виділеного приватного методу для перевірки профілю
        if not self._is_valid_profile(dna_profile):
            raise ValueError("Invalid or missing Voice DNA profile")
        
        # Імітація генерації тексту з обмеженням через константу
        generated_text = f"[Generated LinkedIn Post using {dna_profile}]: {idea.strip()}"
        return generated_text[:self.MAX_POST_LENGTH]

    def schedule_publication(self, content: str, date_str: str) -> bool:
        """
        Метод 3: Валідація та планування відкладеної публікації.
        """
        if not content or len(content.strip()) == 0:
            raise ValueError("Post content cannot be empty")
            
        # Застосування спільної константи ліміту (усунення дублювання)
        if len(content) > self.MAX_POST_LENGTH:
            raise ValueError(f"Post content cannot exceed {self.MAX_POST_LENGTH} characters")
            
        # Використання константи для формату дати
        try:
            scheduled_date = datetime.strptime(date_str, self.DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Invalid date format. Use {self.DATE_FORMAT}")
            
        if scheduled_date <= datetime.now():
            raise ValueError("Scheduled date must be in the future")
            
        return True
