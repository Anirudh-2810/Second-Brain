---
module: "current-projects"
topic: "React Calculator — Keyboard-Supported, History, Tailwind Styled"
tags: [builds, react, calculator, tailwindcss, lucide-react, keyboard-shortcuts, history, hooks, single-file-component, functional-component]
last_updated: "2026-08-26"
confidence: "high"
source: "Desktop/Anirudh/My apps/Calculator/calculator.html (255 lines)"
description: "React calculator component with full keyboard support, calculation history (last 5), gradient UI with Tailwind CSS, Lucide icons, error handling (divide by zero), percentage and sign toggle. Single-file functional component ready for Next.js/Vite. Includes exact state management, keyboard event handling, and button styling system."
---

# React Calculator — Keyboard-Supported, History, Tailwind Styled

> **Source:** `Desktop/Anirudh/My apps/Calculator/calculator.html` (255 lines)
> **Stack:** React 18+, Tailwind CSS, `lucide-react` (icons)
> **Format:** Single-file functional component (JSX)
> **Features:** Mouse + full keyboard, history panel, gradient dark theme

---

## For future agent
This is a **personal frontend build** — a polished calculator React component demonstrating hooks (`useState`, `useEffect`), keyboard event handling, controlled inputs, and Tailwind utility-first styling. Ready to drop into Next.js, Vite, or CRA. Cross-links: [[wiki/01-Areas/Programming/web-development]], [[wiki/01-Areas/Programming/SAAS_BUILD_NOTES]].

---

## 1. Features (Detailed)

| Feature | Implementation | Details |
|---------|----------------|---------|
| **Display** | Current + previous operand + operator preview | Shows `"5 + "` above result, monospace font |
| **History** | Last 5 calculations | Fading opacity (0.6 → 0.15), scrollable container |
| **Keyboard** | `useEffect` + `window.addEventListener` | Numbers, operators, Enter/=, Escape/C, Backspace, . |
| **Operations** | +, -, ×, ÷, %, ±, decimal | Chained operations (5 + 3 × 2 resolves 5+3 first) |
| **Error Handling** | Divide by zero → "Error" state | Resets on next input |
| **Icons** | Lucide React (Delete, Divide, Minus, Plus, X) | 20px, white stroke |
| **Styling** | Tailwind gradients | Dark slate/purple theme, active scale animation |
| **Responsive** | `max-w-md` centered | Works on mobile + desktop |

---

## 2. Component Architecture

### State Management
```javascript
const Calculator = () => {
  // Display state
  const [display, setDisplay] = useState('0');          // Current number shown
  const [previous, setPrevious] = useState('');         // Previous operand
  const [operator, setOperator] = useState('');         // Current operator (+, -, *, /)
  const [newNumber, setNewNumber] = useState(true);     // Flag: next input starts new number
  
  // History state
  const [history, setHistory] = useState([]);           // Array of strings: ["5 + 3 = 8", ...]
  
  // Keyboard effect
  useEffect(() => {
    const handleKeyPress = (e) => { /* ... */ };
    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
  }, [display, previous, operator, newNumber]);  // Dependencies for closure
```

### Component Tree
```
Calculator
├── History Panel (conditional: history.length > 0)
│   └── History Items (map with opacity fade)
├── Display Container
│   ├── Previous + Operator Preview (small, gray)
│   └── Current Display (large, white)
└── Button Grid (grid-cols-4)
    ├── Row 1: AC, ±, %, ÷
    ├── Row 2: 7, 8, 9, ×
    ├── Row 3: 4, 5, 6, -
    ├── Row 4: 1, 2, 3, +
    └── Row 5: 0 (col-span-2), ., =
```

---

## 3. Core Logic — Exact Implementation

### Number Input
```javascript
const handleNumber = (num) => {
  if (newNumber) {
    // First digit of new number
    setDisplay(num);
    setNewNumber(false);
  } else {
    // Append to current number
    setDisplay(display === '0' ? num : display + num);
  }
};
```

### Decimal Point
```javascript
const handleDecimal = () => {
  if (newNumber) {
    setDisplay('0.');
    setNewNumber(false);
    return;
  }
  // Prevent multiple decimals
  if (!display.includes('.')) {
    setDisplay(display + '.');
  }
};
```

### Operator Handling (Chained Operations)
```javascript
const handleOperator = (op) => {
  if (previous && operator && !newNumber) {
    // Resolve pending operation: 5 + 3 → then × is pressed
    handleEquals();  // Calculate 5 + 3 = 8, then set 8 as previous
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
      if (curr === 0) {
        setDisplay('Error');
        setPrevious('');
        setOperator('');
        setNewNumber(true);
        return;
      }
      result = prev / curr; 
      break;
  }
  
  // Add to history (keep last 5)
  const calculation = `${prev} ${operator} ${curr} = ${result}`;
  setHistory([calculation, ...history.slice(0, 4)]);
  
  // Reset state
  setDisplay(result.toString());
  setPrevious('');
  setOperator('');
  setNewNumber(true);
};
```

### Clear & Backspace
```javascript
const handleClear = () => {
  setDisplay('0');
  setPrevious('');
  setOperator('');
  setNewNumber(true);
};

const handleBackspace = () => {
  if (newNumber || display === 'Error') return;
  if (display.length === 1 || (display.length === 2 && display[0] === '-')) {
    setDisplay('0');
    setNewNumber(true);
  } else {
    setDisplay(display.slice(0, -1));
  }
};
```

### Percentage & Sign Toggle
```javascript
const handlePercent = () => {
  const value = parseFloat(display);
  setDisplay((value / 100).toString());
  setNewNumber(true);
};

const handleSignToggle = () => {
  if (display === '0' || display === 'Error') return;
  setDisplay(display.startsWith('-') ? display.slice(1) : '-' + display);
};
```

---

## 4. Keyboard Event Handling

```javascript
useEffect(() => {
  const handleKeyPress = (e) => {
    // Prevent default for calculator keys
    if (['Enter', 'Escape', 'Backspace'].includes(e.key)) {
      e.preventDefault();
    }
    
    // Number keys
    if (e.key >= '0' && e.key <= '9') {
      handleNumber(e.key);
      return;
    }
    
    // Operators
    const keyToOperator = {
      '+': '+',
      '-': '-',
      '*': '*',
      '/': '/'
    };
    if (keyToOperator[e.key]) {
      handleOperator(keyToOperator[e.key]);
      return;
    }
    
    // Other keys
    switch (e.key) {
      case '.':
        handleDecimal();
        break;
      case 'Enter':
      case '=':
        handleEquals();
        break;
      case 'Escape':
      case 'c':
      case 'C':
        handleClear();
        break;
      case 'Backspace':
        handleBackspace();
        break;
      case '%':
        handlePercent();
        break;
    }
  };
  
  window.addEventListener('keydown', handleKeyPress);
  return () => window.removeEventListener('keydown', handleKeyPress);
}, [display, previous, operator, newNumber]);
// Dependencies: re-attach when these change (closure updates)
```

### Key Mapping Reference
| Key | Action | Handler |
|-----|--------|---------|
| `0-9` | Input digit | `handleNumber(key)` |
| `.` | Decimal point | `handleDecimal()` |
| `+`, `-`, `*`, `/` | Set operator | `handleOperator(key)` |
| `Enter` / `=` | Calculate | `handleEquals()` |
| `Escape` / `C` | Clear all | `handleClear()` |
| `Backspace` | Delete last | `handleBackspace()` |
| `%` | Percentage | `handlePercent()` |

---

## 5. UI Structure — Complete JSX

```jsx
return (
  <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 flex items-center justify-center p-4">
    <div className="w-full max-w-md">
      <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-3xl shadow-2xl p-6 border border-slate-700">
        
        {/* History Panel */}
        {history.length > 0 && (
          <div className="mb-4 space-y-1 h-20 overflow-hidden">
            {history.map((calc, i) => (
              <div 
                key={i} 
                className="text-slate-400 text-xs font-mono text-right"
                style={{ opacity: 0.6 - i * 0.15 }}  // Fading opacity
              >
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
          {/* Row 1: AC, ±, %, ÷ */}
          <Button onClick={handleClear} className="bg-gradient-to-b from-red-500 to-red-600 text-white shadow-lg shadow-red-500/30">
            AC
          </Button>
          <Button onClick={handleSignToggle} className="bg-gradient-to-b from-slate-600 to-slate-700 text-white">
            ±
          </Button>
          <Button onClick={handlePercent} className="bg-gradient-to-b from-slate-600 to-slate-700 text-white">
            %
          </Button>
          <Button onClick={() => handleOperator('/')} className="bg-gradient-to-b from-orange-500 to-orange-600 text-white shadow-lg shadow-orange-500/30">
            <Delete size={20} />
          </Button>
          
          {/* Row 2: 7, 8, 9, × */}
          <Button onClick={() => handleNumber('7')}>7</Button>
          <Button onClick={() => handleNumber('8')}>8</Button>
          <Button onClick={() => handleNumber('9')}>9</Button>
          <Button onClick={() => handleOperator('*')} className="bg-gradient-to-b from-orange-500 to-orange-600 text-white shadow-lg shadow-orange-500/30">
            <X size={20} />
          </Button>
          
          {/* Row 3: 4, 5, 6, - */}
          <Button onClick={() => handleNumber('4')}>4</Button>
          <Button onClick={() => handleNumber('5')}>5</Button>
          <Button onClick={() => handleNumber('6')}>6</Button>
          <Button onClick={() => handleOperator('-')} className="bg-gradient-to-b from-orange-500 to-orange-600 text-white shadow-lg shadow-orange-500/30">
            <Minus size={20} />
          </Button>
          
          {/* Row 4: 1, 2, 3, + */}
          <Button onClick={() => handleNumber('1')}>1</Button>
          <Button onClick={() => handleNumber('2')}>2</Button>
          <Button onClick={() => handleNumber('3')}>3</Button>
          <Button onClick={() => handleOperator('+')} className="bg-gradient-to-b from-orange-500 to-orange-600 text-white shadow-lg shadow-orange-500/30">
            <Plus size={20} />
          </Button>
          
          {/* Row 5: 0 (span 2), ., = */}
          <Button onClick={() => handleNumber('0')} span>0</Button>
          <Button onClick={handleDecimal}>.</Button>
          <Button onClick={handleEquals} className="bg-gradient-to-b from-green-500 to-green-600 text-white shadow-lg shadow-green-500/30">
            =
          </Button>
        </div>
      </div>
    </div>
  </div>
);
```

---

## 6. Button Component & Styling System

### Button Component
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
```

### Color Scheme Reference
| Button Type | Tailwind Classes | Hex Values |
|-------------|------------------|------------|
| **Numbers** | `from-slate-700 to-slate-800 text-white` | `#334155` → `#1e293b` |
| **Operators** | `from-orange-500 to-orange-600 text-white shadow-orange-500/30` | `#f97316` → `#ea580c` |
| **AC (Clear)** | `from-red-500 to-red-600 text-white shadow-red-500/30` | `#ef4444` → `#dc2626` |
| **= (Equals)** | `from-green-500 to-green-600 text-white shadow-green-500/30` | `#22c55e` → `#16a34a` |
| **Backspace, ±** | `from-slate-600 to-slate-700 text-white` | `#475569` → `#334155` |

### Animation
```css
/* Tailwind transition utilities */
transition-all duration-150  /* Smooth transitions */
active:scale-95              /* Press effect: scale down 5% */
```

---

## 7. Integration Examples

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

function App() {
  return <Calculator />;
}

export default App;
```

### Create React App
```jsx
// src/App.js
import Calculator from './Calculator';

function App() {
  return (
    <div className="App">
      <Calculator />
    </div>
  );
}

export default App;
```

### Tailwind Configuration
```javascript
// tailwind.config.js
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      // Optional: custom calculator colors
      colors: {
        calc: {
          number: '#334155',
          operator: '#f97316',
          clear: '#ef4444',
          equals: '#22c55e'
        }
      }
    }
  },
  plugins: [],
}
```

---

## 8. Cross-References

- [[wiki/01-Areas/Programming/web-development]] — Frontend resources, React patterns
- [[wiki/01-Areas/Programming/SAAS_BUILD_NOTES]] — Next.js + Tailwind + shadcn/ui stack
- [[wiki/01-Areas/Programming/learn-python-fast-system]] — Full-stack project structure

---

## 9. Known Limitations / TODOs (Detailed)

| Limitation | Impact | Fix |
|------------|--------|-----|
| **No scientific functions** | Can't do sin, cos, log, pow, parentheses | Add scientific mode toggle |
| **No memory keys** | M+, M-, MR, MC not available | Add memory state + buttons |
| **History not persisted** | Lost on unmount | Add `localStorage` persistence |
| **No theme toggle** | Dark only | Add light mode with theme context |
| **Single-file** | 255 lines, hard to maintain | Split into Display, Keypad, History sub-components |
| **No tests** | No Jest/RTL coverage | Add unit tests for all handlers |
| **No TypeScript** | No type safety | Convert to `.tsx` with interfaces |
| **No responsive design** | Fixed `max-w-md` | Add mobile-first responsive breakpoints |

---

## 10. Code Statistics

| Metric | Value |
|--------|-------|
| **Total Lines** | 255 |
| **Component Count** | 1 (single-file) |
| **Hooks Used** | `useState` (5), `useEffect` (1) |
| **Event Listeners** | `keydown` (keyboard) |
| **Button Count** | 19 (0-9, +, -, *, /, %, ±, ., =, AC) |
| **State Variables** | 6 (display, previous, operator, newNumber, history, ...) |
| **Keyboard Shortcuts** | 12 unique keys |

---

## See Also
- [[wiki/01-Areas/Programming/web-development/web-development-resources]] — React + Tailwind resources
- [[wiki/01-Areas/Programming/SAAS_BUILD_NOTES]] — Production React patterns
- [[wiki/00-Current-Projects/budget-tracker]] — Another personal tool (Excel/VBA)