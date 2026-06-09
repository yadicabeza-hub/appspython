const display = document.getElementById('display');
let currentValue = '0';
let previousValue = null;
let operator = null;
let waitingForSecondValue = false;

function updateDisplay() {
  display.textContent = currentValue;
}

function inputNumber(number) {
  if (waitingForSecondValue) {
    currentValue = number;
    waitingForSecondValue = false;
    return;
  }

  if (currentValue === '0') {
    currentValue = number;
  } else {
    currentValue += number;
  }
}

function inputDecimal() {
  if (waitingForSecondValue) {
    currentValue = '0.';
    waitingForSecondValue = false;
    return;
  }

  if (!currentValue.includes('.')) {
    currentValue += '.';
  }
}

function clearCalculator() {
  currentValue = '0';
  previousValue = null;
  operator = null;
  waitingForSecondValue = false;
}

function toggleSign() {
  if (currentValue === '0') return;
  currentValue = currentValue.startsWith('-') ? currentValue.slice(1) : `-${currentValue}`;
}

function percentValue() {
  currentValue = String(parseFloat(currentValue) / 100);
}

function calculate() {
  const current = parseFloat(currentValue);
  const previous = parseFloat(previousValue);
  if (operator === null || previousValue === null || Number.isNaN(previous) || Number.isNaN(current)) {
    return;
  }

  let result = 0;
  switch (operator) {
    case '+':
      result = previous + current;
      break;
    case '-':
      result = previous - current;
      break;
    case '*':
      result = previous * current;
      break;
    case '/':
      result = current === 0 ? 'Error' : previous / current;
      break;
    default:
      return;
  }

  currentValue = String(result);
  operator = null;
  previousValue = null;
  waitingForSecondValue = false;
}

function handleOperator(nextOperator) {
  const inputValue = parseFloat(currentValue);

  if (operator && waitingForSecondValue) {
    operator = nextOperator;
    return;
  }

  if (previousValue === null) {
    previousValue = currentValue;
  } else if (operator) {
    const result = performCalculation(operator, parseFloat(previousValue), inputValue);
    currentValue = String(result);
    previousValue = currentValue;
  }

  operator = nextOperator;
  waitingForSecondValue = true;
}

function performCalculation(operator, first, second) {
  switch (operator) {
    case '+':
      return first + second;
    case '-':
      return first - second;
    case '*':
      return first * second;
    case '/':
      return second === 0 ? 'Error' : first / second;
    default:
      return second;
  }
}

const buttons = document.querySelector('.buttons');
buttons.addEventListener('click', (event) => {
  const target = event.target;
  if (!target.matches('button')) return;

  const action = target.dataset.action;
  const value = target.dataset.value;

  switch (action) {
    case 'number':
      inputNumber(value);
      break;
    case 'decimal':
      inputDecimal();
      break;
    case 'clear':
      clearCalculator();
      break;
    case 'toggle-sign':
      toggleSign();
      break;
    case 'percent':
      percentValue();
      break;
    case 'operator':
      handleOperator(value);
      break;
    case 'calculate':
      calculate();
      break;
    default:
      return;
  }

  updateDisplay();
});

updateDisplay();
