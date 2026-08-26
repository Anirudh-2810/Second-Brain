---
module: "current-projects"
topic: "React Calculator — Keyboard-Supported, History, Tailwind Styled"
tags: [builds, react, calculator, tailwindcss, lucide-react, keyboard-shortcuts, history, hooks]
last_updated: "2026-08-26"
confidence: "high"
source: "Desktop/Anirudh/My apps/Calculator/calculator.html"
description: "React calculator component with full keyboard support, calculation history (last 5), gradient UI with Tailwind CSS, Lucide icons, error handling (divide by zero), percentage and sign toggle. Single-file component ready for Next.js/Vite."
---

# React Calculator — Keyboard-Supported, History, Tailwind Styled

> **Source:** `Desktop/Anirudh/My apps/Calculator/calculator.html`
> **Stack:** React 18+, Tailwind CSS, `lucide-react` (icons)
> **Format:** Single-file functional component (JSX)
> **Features:** Mouse + full keyboard, history panel, gradient dark theme

---

## For future agent
This is a **personal frontend build** — a polished calculator React component demonstrating hooks (`useState`, `useEffect`), keyboard event handling, controlled inputs, and Tailwind utility-first styling. Ready to drop into Next.js, Vite, or CRA. Cross-links: [[wiki/01-Areas/Programming/web-development]], [[wiki/01-Areas/Programming/SAAS_BUILD_NOTES]].

---

## 1. Features

| Feature | Implementation |
|---------|----------------|
| **Display** | Current + previous operand + operator preview |
| **History** | Last 5 calculations, fading opacity, scrollable |
| **Keyboard** | Numbers, operators, Enter/=, Escape/C, Backspace, . |
| **Operations** | +, -, ×, ÷, %, ±, decimal |
| **Error Handling** | Divide by zero → "Error" state |
| **Icons** | Lucide React (Delete, Divide, Minus, Plus, X) |
| **Styling** | Tailwind gradients, dark slate/purple theme, active scale animation |

---

## 2. Component API

```jsx
import Calculator from './Calculator';

// Drop into any React app
<Calculator />
```

**Props:** None (self-contained)

**State:**
```javascript
const [display, setDisplay] = useState('0');
const [previous, setPrevious] = useState('');
const [operator, setOperator] = useState('');
const [newNumber, setNewNumber] = useState(true);
const [history, setHistory] = useState([]);
```

---

## 3. Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Input digit |
| `.` | Decimal point |
| `+`, `-`, `*`, `/` | Set operator |
| `Enter` / `=` | Calculate result |
| `Escape` / `C` / `c` | Clear all |
| `Backspace` | Delete last digit |

```javascript
useEffect(() => {
  const handleKeyPress = (e) => {
    if (e.key >= '0' && e.key <= '9') handleNumber(e.key);
    else if (e.key === '.') handleDecimal();
    else if (['+', '-', '*', '/'].includes(e.key)) handleOperator(e.key);
    else if (e.key === 'Enter' || e.key === '=') handleEquals();
    else if (e.key === 'Escape' || e.key.toLowerCase() === 'c') handleClear();
    else if (e.key === 'Backspace') handleBackspace();
  };
  window.addEventListener('keydown', handleKeyPress);
  return () => window.removeEventListener('keydown', handleKeyPress);
}, [display, previous, operator, newNumber]);
```

---

## 4. Core Logic

### Number Input
```javascript
const handleNumber = (num) => {
  if (newNumber) {
    setDisplay(num);
    setNewNumber(false);
  } else {
    setDisplay(display === '0' ? num : display + num);
  }
};
```

### Operator Handling (Chained Operations)
```javascript
const handleOperator = (op) => {
  if (previous && operator && !newNumber) {
    handleEquals();  // Resolve pending operation first
  }
  setPrevious(display);
  setOperator(op);
  setNewNumber(true);
};
```

### Equals (with History)
```javascript
const handleEquals = () => {
  if (!previous || !operator) return;
  const prev = parseFloat(previous);
  const curr = parseFloat(display);
  let result;
  switch (operator) {
    case '+': result = prev + curr; break;
    case '-': result = prev - curr; break;
    case '*': result = prev * curr; break;
    case '/': 
      if (curr === 0) { setDisplay('Error'); /* reset */; return; }
      result = prev / curr; break;
  }
  const calculation = `${prev} ${operator} ${curr} = ${result}`;
  setHistory([calculation, ...history.slice(0, 4)]);  // Keep last 5
  setDisplay(result.toString());
  setPrevious(''); setOperator(''); setNewNumber(true);
};
```

---

## 5. UI Structure

```jsx
<div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 flex items-center justify-center p-4">
  <div className="w-full max-w-md">
    <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-3xl shadow-2xl p-6 border border-slate-700">
      {/* History Panel */}
      {history.length > 0 && (
        <div className="mb-4 space-y-1 h-20 overflow-hidden">
          {history.map((calc, i) => (
            <div key={i} className="text-slate-400 text-xs font-mono text-right opacity-60"
              style={{ opacity: 0.6 - i * 0.15 }}>
              {calc}
            </div>
          ))}
        </div>
      )}
      
      {/* Display */}
      <div className="bg-gradient-to-br from-slate-700 to-slate-800 rounded-2xl p-6 mb-6 border border-slate-600">
        <div className="text-slate-400 text-sm mb-1 h-6 font-mono">
          {previous && operator && `${previous} ${operator}`}
        </div>
        <div className="text-white text-right text-4xl font-bold break-all">
          {display}
        </div>
      </div>
      
      {/* Button Grid */}
      <div className="grid grid-cols-4 gap-3">
        {/* Buttons with gradient classes */}
      </div>
    </div>
  </div>
</div>
```

---

## 6. Button Styling System

```jsx
const Button = ({ children, onClick, className = '', span = false }) => (
  <button
    onClick={onClick}
    className={`h-16 rounded-xl font-semibold text-lg transition-all duration-150 active:scale-95 ${
      span ? 'col-span-2' : ''
    } ${className}`}
  >
    {children}
  </button>
);

// Color scheme:
// Numbers: slate-700 → slate-800
// Operators: orange-500 → orange-600 (shadow orange-500/30)
// AC: red-500 → red-600 (shadow red-500/30)
// =: green-500 → green-600 (shadow green-500/30)
// Backspace, ±: slate-600 → slate-700
```

---

## 7. Integration

### Next.js (App Router)
```jsx
// app/calculator/page.tsx
'use client';
import Calculator from '@/components/Calculator';
export default function CalculatorPage() {
  return <Calculator />;
}
```

### Vite + React
```jsx
// src/App.jsx
import Calculator from './Calculator';
function App() { return <Calculator />; }
export default App;
```

### Tailwind Config (if custom colors needed)
```javascript
// tailwind.config.js
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: { extend: {} },
  plugins: [],
}
```

---

## 8. Cross-References

- [[wiki/01-Areas/Programming/web-development]] — Frontend resources, React patterns
- [[wiki/01-Areas/Programming/SAAS_BUILD_NOTES]] — Next.js + Tailwind + shadcn/ui stack
- [[wiki/01-Areas/Programming/learn-python-fast-system]] — Full-stack project structure

---

## 9. Known Limitations / TODOs

- **No scientific functions** — sin, cos, log, pow, parentheses
- **No memory keys** — M+, M-, MR, MC
- **History not persisted** — lost on unmount (add localStorage)
- **No theme toggle** — dark only
- **Single-file** — could split into Display, Keypad, History sub-components
- **No tests** — add Jest/React Testing Library cases

---

## See Also
- [[wiki/01-Areas/Programming/web-development/web-development-resources]] — React + Tailwind resources
- [[wiki/01-Areas/Programming/SAAS_BUILD_NOTES]] — Production React patterns