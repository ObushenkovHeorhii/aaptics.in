Aaptics — це SaaS-платформа на базі штучного інтелекту для активних авторів LinkedIn, яка вирішує проблему шаблонного тексту завдяки технології "Voice DNA", що аналізує та вивчає індивідуальний стиль користувача.

- FR-01: Система повинна дозволяти реєстрацію та авторизацію через email або Google.
- FR-02: Система повинна інтегруватися з API LinkedIn за протоколом OAuth 2.0.  
- FR-03: Система повинна дозволяти завантаження 3-4 старих текстів користувача для формування профілю "Voice DNA". 
- FR-04: Система повинна генерувати текст посту на основі короткої ідеї та збереженого стилю.
- FR-06: Користувач повинен мати можливість запланувати відкладену публікацію.


<img width="826" height="452" alt="Use Case Diagram" src="https://github.com/user-attachments/assets/4af0eece-d00d-4e9a-a725-94532026480c" />

```plantuml
@startuml
left to right direction
actor "Зареєстрований користувач" as User
actor "Адміністратор" as Admin


usecase "Авторизація та підключення LinkedIn" as UC01
usecase "Навчання моделі Voice DNA" as UC02
usecase "Генерація посту" as UC03
usecase "Відкладена публікація" as UC04
usecase "Керування історією" as UC05
usecase "Управління акаунтами та моніторинг" as UC06


User --> UC01
User --> UC02
User --> UC03
User --> UC04
User --> UC05

Admin --> UC06

UC03 ..> UC02 : <<include>>
@enduml

```

<img width="805" height="502" alt="Class Diagram" src="https://github.com/user-attachments/assets/a01dcb0d-dcc2-4caf-aa4b-973088b13732" />


```plantuml
@startuml
class User {
  - userId : String
  - email : String
  - linkedInToken : String
  + authenticate() : boolean
  + deleteAccount() : void
}

class VoiceDNA {
  - dnaId : String
  - styleProfile : String
  + analyzeTexts(texts : List<String>) : void
  + getStyleProfile() : String
}

class Post {
  - postId : String
  - content : String
  - scheduledDate : Date
  - isPublished : boolean
  + schedule(date : Date) : void
  + publishToLinkedIn() : boolean
}

class AIGeneratorService {
  + generateContent(idea : String, style : String) : String
  + generateImage(idea : String) : String
}

class LinkedInIntegration {
  + oauthConnect() : String
  + sendPost(content : String) : boolean
}

User -- VoiceDNA : має
User  -- Post : створює
Post ..> AIGeneratorService : використовує для генерації
Post ..> LinkedInIntegration : використовує для публікації
@enduml

```

<img width="699" height="530" alt="Sequence Diagram" src="https://github.com/user-attachments/assets/35ad0680-779e-4936-9670-444ef0ddcce3" />


```plantuml
@startuml
actor "Користувач" as U
participant ":B Studio (UI)" as UI
participant ":VoiceDNA" as DNA
participant ":AIGenerator" as AI
participant ":Post" as P

U -> UI : ввести ідею для посту
UI -> DNA : getStyleProfile()
DNA --> UI : styleProfile (стиль автора)
UI -> AI : generateContent(idea, styleProfile)

alt успішна генерація ШІ
  AI --> UI : згенерований текст
  U -> UI : натиснути "Запланувати" (дата)
  UI -> P : new Post(text, дата)
  P --> UI : пост збережено
  UI --> U : "Успішно заплановано"
else помилка API
  AI --> UI : помилка таймауту
  UI --> U : "Спробуйте ще раз"
end
@enduml

```

### Матриця трасовності

| Вимога | Use Case | Класи | Sequence Diagram |
| --- | --- | --- | --- |
| **FR-01** (Реєстрація)
| UC-01 | User | — |
| **FR-02** (Інтеграція LinkedIn)
| UC-01 | User, LinkedInIntegration | — |
| **FR-03** (Створення Voice DNA)
| UC-02 | User, VoiceDNA | — |
| **FR-04** (Генерація посту)
| UC-03 | VoiceDNA, Post, AIGeneratorService | SD-01 (Генерація посту) |
| **FR-06** (Планування)
| UC-04 | Post | SD-01 (фрагмент) |
