# Cognitive Study Planner — Frontend Integration & UX

React + Vite single-page app for interactive schedule generation with real-time validation and detailed schedule visualization.

---

## 🎯 User Experience Flow

### 1. User Input Form
**Component:** `UserForm.jsx`

Users specify their state:
- **Sleep Hours** [0.0 – 16.0]: Discrete input with 0.25 step
- **Stress Level** [1 – 5]: Integer with visual label (low ↔ high)
- **Preferred Time of Day** [dropdown]:
  - Morning (06:00–12:00 optimal for hard tasks)
  - Afternoon (12:00–17:00)
  - Evening (17:00–21:00)
  - Night (21:00–02:00)

**Validation (Client-Side):**
- Min/max enforced on input type="number"
- Stress clamped to integer via `Math.round()`
- Sleep clamped to [0, 16]
- Helper text guides users

**UX Details:**
- Real-time clamping (value corrects as user types)
- Color-coded helper text (gray for info, orange for warning)
- Accessible labels and semantic HTML

---

### 2. Task Queue Input
**Component:** `TaskInput.jsx`

Users add multiple tasks:
- **Title** [text]: "Solve DP problems", "Read Chapter 4"
- **Time** [integer, minutes]: [5 – 300], step 5
- **Subject** [dropdown]: dsa, math, physics, english, history, coding

**Smart Validation (Real-Time):**
- Title required and non-empty
- Time clamped to [5, 300]
- Remaining allocatable minutes displayed (720 total max)
- Add button disabled when constraints violated
- Tooltip explains why button is disabled

**User Feedback:**
- "Remaining allocatable minutes: X" (updates as tasks added)
- Color change: orange when <60 mins remain, red when 0
- Alert on add failure with reason

**Edge Cases:**
- User adds 700m of work, then tries 50m task: prevented with message
- User enters 999m: clamped to 300m on blur
- User enters 0: clamped to 5m
- User deletes a task: remaining minutes recalculate immediately

---

### 3. Task Queue Display
**Component:** `TaskList.jsx`

Shows queued tasks before generation:
- Task title
- **Difficulty badge** (new feature): EASY (green) | MEDIUM (yellow) | HARD (red)
- Time in minutes
- Subject tag
- Delete button (X icon with hover animation)

**Rationale for Difficulty Display:**
- User sees what tasks backend classified as hard before scheduling
- Provides confidence that system understands task complexity
- Informs user about final schedule distribution

---

### 4. Generate & Schedule Output
**Component:** `ScheduleView.jsx`

After clicking "Generate Optimized Schedule":
- Shows loader animation while computing
- Displays final schedule as timeline

**Schedule Item Display:**
- **Time Slot**: "08:00 – 10:00" (formatted, normalized)
- **Task Title** + **Difficulty Badge** (EASY/MEDIUM/HARD, color-coded)
- **Efficiency Bar**: Visual representation of expected_efficiency
  - Green (≥80%): Optimal cognitive fit
  - Orange (50–80%): Good fit with some fatigue
  - Red (<50%): Suboptimal (scheduled in fatigue trough, but necessary)
- **Efficiency Percentage**: "82%" numeric display

**Timeline Visual:**
- Vertical timeline with dots colored by efficiency
- Left border colored by difficulty
- Hover effects for interactivity
- Print-friendly styling

**Rationale:**
- Efficiency color + percentage explains *why* each task is placed when
- User can see cumulative fatigue building (later tasks lower efficiency)
- Validates that hard tasks got preferred window placement

---

## 🏗️ Frontend Architecture

### Component Hierarchy

```
App (pages/index.jsx)
  └─ State Management
      ├─ userState
      ├─ taskInput
      ├─ tasks
      └─ schedule
  │
  ├─ UserForm
  │   └─ handleUserChange (with validation)
  │
  ├─ TaskInput
  │   ├─ handleTaskChange (with clamping)
  │   ├─ addTask (with checks)
  │   └─ remainingMinutes (computed)
  │
  ├─ TaskList
  │   └─ tasks.map(render with difficulty)
  │
  ├─ Generate Button
  │   └─ handleGenerate (calls API)
  │
  ├─ Loader (conditional)
  │
  └─ ScheduleView
      └─ schedule.map(render with efficiency)
```

### Data Flow

```
User Input
  ↓ (onChange handlers)
Component State Update
  ↓ (validation + clamping on client)
API Payload Built
  ↓ (POST /schedule/generate)
Backend Processing
  ↓ (pipeline: energy → classification → scheduling → efficiency)
Response Received
  ↓ (extract schedule + classificationdiffiulties)
Update Local State
  ↓ (attach difficulty badges to task queue)
Render Output (ScheduleView)
```

---

## 📋 Input Validation Strategy (Layered)

### Layer 1: HTML Input Constraints
```jsx
<input type="number" min="0" max="16" step="0.25" />
```
- Browser prevents typing most invalid values
- Keyboard sanitization

### Layer 2: onChange Handler (React)
```javascript
handleUserChange(e) {
  const name = e.target.name;
  const raw = e.target.value;
  
  if (name === "sleep_hours") {
    let v = Number(raw);
    v = Math.max(0, Math.min(16, v));
    setUserState({ ...userState, sleep_hours: v });
  }
}
```
- Real-time clamping
- Immediate feedback
- Sanitizes pasted/autocompleted values

### Layer 3: Button Disable Logic
```javascript
const isFormValid = titleValid && timeValid && fitsRemaining;
<button disabled={!isFormValid} />
```
- Prevents invalid submissions
- Clear visual feedback

### Layer 4: Backend Re-Validation
- Pydantic schemas enforce types and ranges
- Returns 422 (Unprocessable Entity) if invalid
- Frontend shows alert to user

**Rationale:** Multiple layers ensure robustness without being intrusive.

---

## 🎨 Visual Design & UX

### Color Scheme
- **Difficulty Colors:**
  - Easy: Green (#34d399)
  - Medium: Orange (#f59e0b)
  - Hard: Red (#ef4444)
- **Efficiency Colors:**
  - High (≥80%): Green (#10b981)
  - Medium (50–80%): Orange (#f59e0b)
  - Low (<50%): Red (#ef4444)

### Interactive Elements
- **Buttons:** Hover effects, disabled state
- **Inputs:** Focus states, placeholder text, helper text
- **Badges:** Pill-shaped, uppercase, bold
- **Bars:** Smooth animations, gradient backgrounds

### Accessibility
- Semantic HTML (`<label>`, `<button>`, `<input>`)
- ARIA labels for screen readers
- Color not sole indicator (text + icons)
- Keyboard navigation supported

---

## 🔄 State Management

**App-Level State:**
```javascript
const [userState, setUserState] = useState({
  sleep_hours: 7,
  stress_level: 3,
  time_of_day: "morning"
});

const [taskInput, setTaskInput] = useState({
  title: "",
  estimated_time: 30,
  subject: "dsa"
});

const [tasks, setTasks] = useState([]);
const [schedule, setSchedule] = useState(null);
const [isLoading, setIsLoading] = useState(false);
```

**Derived State:**
```javascript
const totalMinutes = tasks.reduce((s, t) => s + t.estimated_time, 0);
const remainingMinutes = Math.max(0, 720 - totalMinutes);
```

**Update Flow:**
- User input → setState() → re-render
- Add task → validate → push to array → re-render
- Generate → setIsLoading(true) → API call → setSchedule() → setIsLoading(false)

---

## 📡 API Integration (services/api.js)

**generateSchedule(data):**
```javascript
export const generateSchedule = (data) => {
  return API.post("/schedule/generate", data);
};
```

**Usage in App:**
```javascript
const res = await generateSchedule({
  user_state: userState,
  tasks: tasks
});

const schedule = res.data.schedule || [];
setSchedule(schedule);

// Attach difficulties back to task queue for display
if (Array.isArray(schedule)) {
  const diffMap = {};
  schedule.forEach(s => {
    if (s.task && s.difficulty) {
      diffMap[s.task] = s.difficulty;
    }
  });
  setTasks(prev => prev.map(t => ({ ...t, difficulty: diffMap[t.title] })));
}
```

**Error Handling:**
```javascript
catch (err) {
  console.error(err);
  alert("Error generating schedule. Ensure backend is running.");
}
```

---

## 🚀 Performance Optimizations

- **Memoization:** useMemo for remainingMinutes calculation (if tasks change frequently)
- **Lazy Loading:** ScheduleView only renders when schedule exists
- **Debouncing:** Validation logic runs on onChange (fast, sub-100ms)
- **Bundle Size:** Vite tree-shakes unused code; React production build ~40KB gzipped

---

## 🧪 Testing Scenarios

### Scenario 1: Happy Path
1. User enters sleep=8, stress=2, time=morning
2. Adds 3 tasks (30m easy, 60m medium, 120m hard)
3. Clicks Generate
4. **Expected:** Schedule with hard task 08:00–10:00, others around it, all efficiency scores ≥0.6

### Scenario 2: Edge Case: Max Load
1. User adds 6 tasks × 120m = 720 minutes (max)
2. Try to add 7th task (any duration)
3. **Expected:** Add button disabled, message "No remaining minutes available"

### Scenario 3: Edge Case: Extreme Inputs
1. Sleep = 0 (no sleep), Stress = 5 (max stress)
2. Add mixed tasks
3. **Expected:** Energy predicted low (~0.2); schedule easy tasks earlier, hard tasks later, efficiency <0.5

### Scenario 4: Network Error
1. Backend unavailable
2. Click Generate
3. **Expected:** Loader shows, then alert "Error generating schedule"

---

## 📝 Component API Reference

### UserForm
```javascript
<UserForm 
  userState={{ sleep_hours, stress_level, time_of_day }}
  handleUserChange={(e) => {...}}
/>
```

### TaskInput
```javascript
<TaskInput 
  taskInput={{ title, estimated_time, subject }}
  handleTaskChange={(e) => {...}}
  addTask={() => {...}}
  remainingMinutes={integer}
/>
```

### TaskList
```javascript
<TaskList 
  tasks={array}
  deleteTask={(index) => {...}}
/>
```

### ScheduleView
```javascript
<ScheduleView 
  schedule={array}
/>
```

---

## 🔗 Integration Points with Backend

1. **User State Validation:**
   - Frontend clamps values
   - Backend re-validates

2. **Task Classification:**
   - Frontend: sends title, estimated_time, subject
   - Backend: returns difficulty
   - Frontend: attaches difficulty to task queue display

3. **Schedule Generation:**
   - Frontend: sends user_state + tasks
   - Backend: orchestrates pipeline
   - Frontend: receives schedule with time_slot, difficulty, expected_efficiency
   - Frontend: renders timeline with efficiency visualization

---

## 🎯 UX Principles Applied

1. **Clarity:** Every input, output, and action has a clear purpose and visual feedback
2. **Guidance:** Helper text explains constraints (e.g., "5–300 minutes")
3. **Feedback:** Real-time validation prevents errors before they happen
4. **Accessibility:** Semantic HTML, colors + text, keyboard support
5. **Efficiency:** Minimal steps from input to result (3 main sections)
6. **Trust:** Show rationale (difficulty badges, efficiency scores) so user understands why schedule is structured that way

---

## 📦 Dependencies

- **React 18+:** State, hooks, JSX
- **Vite:** Fast build tool, dev server
- **Axios:** API client
- **CSS:** Custom stylesheets (no CSS framework, minimal bundle)

---

## 🚀 Running Locally

```bash
cd frontend
npm install
npm run dev
```

**Output:** http://localhost:5173

---

See also: backend/README_DESIGN.md for backend architecture details.
