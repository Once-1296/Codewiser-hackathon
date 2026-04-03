# 🧠 Cognitive Study Planner (ML-Powered)

A full-stack ML-based system that generates optimized study schedules based on user energy levels and task difficulty.

---

## 🚀 Features

- 🔋 Energy prediction (sleep, stress, time of day)
- 📚 Task difficulty classification (time + subject + keywords)
- 🧠 Intelligent scheduling engine
- 🌐 REST API (FastAPI)
- 🗄️ SQLite DB for persistence
- 🧪 Full test coverage (ML, services, API, DB)
- 📊 Model evaluation with metrics + graphs
- 🛡️ Fallback logic (works even without trained models)

---

## 🏗️ Architecture

User Input
↓
API Layer (FastAPI)
↓
Schemas (Pydantic)
↓
Services Layer (Orchestration)
↓
ML Layer (Predictors)
↓
Scheduler Engine
↓
Response


---

## 🧠 ML Pipeline

### 1. Data
- Synthetic dataset generation (`dataset_loader.py`)
- Controlled + reproducible

### 2. Features
- Energy:
  - sleep_norm
  - stress_norm
  - time_score
- Task:
  - estimated_time
  - subject_score
  - keyword_score

### 3. Models
- Energy → `RandomForestRegressor`
- Task → `DecisionTreeClassifier`

### 4. Fallbacks
- Rule-based prediction if model not available

---

## 📊 Evaluation

Run:

```bash
python -m backend.training.evaluate

Outputs:

    Energy:

        MSE

        R² score

        Scatter plot (energy_eval.png)

    Task:

        Accuracy

        Classification report

        Distribution plot (task_eval.png)

🧪 Testing

Run:

pytest

Covers:

    ML logic

    Services

    API routes

    DB operations

    Training data

🗄️ Database

    SQLite (auto-created)

    Tables:

        user_states

        tasks

▶️ Running the Server

uvicorn backend.app.main:app --reload

Docs:

http://127.0.0.1:8000/docs

⚠️ Important Notes

    No LLMs used (constraint compliant)

    ML + rule-based hybrid system

    Feature consistency maintained across:

        training

        evaluation

        inference

🔥 Future Improvements

    Smarter scheduling (breaks, fatigue)

    Real-world datasets

    User history tracking

    Frontend integration


---

# 🎨 FRONTEND LAYOUT (Fast + Clean + Demo-Ready)

We’ll keep it:
- minimal UI
- strong UX
- API-first

---

# 🧠 Core Idea

Single-page app with 3 sections:

[ User State ] + [ Tasks Input ] → [ Generate ] → [ Schedule Output ]


---

# 📁 Suggested Frontend Structure (React / Next)

frontend/
├── components/
│ ├── UserForm.tsx
│ ├── TaskInput.tsx
│ ├── TaskList.tsx
│ ├── ScheduleView.tsx
│ └── Loader.tsx
├── services/
│ └── api.ts
├── pages/
│ └── index.tsx
├── styles/
└── types/


---

# 🧩 UI Breakdown

## 1. 🔋 User State Form

Fields:
- sleep_hours (slider 0–10)
- stress_level (1–5)
- time_of_day (dropdown)

---

## 2. 📚 Task Input

Each task:
- title (text)
- estimated_time (number)
- subject (dropdown)

+ “Add Task” button

---

## 3. 🚀 Generate Button

Calls:

POST /schedule/generate


---

## 4. 📅 Schedule Output

Display as:

18:00–19:00 → Solve DSA (Efficiency: 0.82)
19:00–19:30 → Read Notes (Efficiency: 0.65)


---

# 🔌 API Integration

## 📁 `services/api.ts`

```ts
export async function generateSchedule(data: any) {
  const res = await fetch("http://127.0.0.1:8000/schedule/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return res.json();
}

🧠 UX Flow

    User fills form

    Adds tasks

    Clicks generate

    Show loader

    Render schedule

🎨 Optional (but HIGH impact)

    color code tasks:

        🔴 hard

        🟡 medium

        🟢 easy

    progress bar for efficiency

    simple timeline UI
