#!/usr/bin/env python3
"""
Продвинутый калькулятор 2025
Современный калькулятор с научными функциями, историей и конвертацией единиц
"""

import math
import re
from typing import List, Dict, Tuple, Optional
from datetime import datetime
import json
import os


class Calculator2025:
    """Класс продвинутого калькулятора с расширенными возможностями"""

    def __init__(self):
        self.history: List[Dict] = []
        self.memory: float = 0.0
        self.variables: Dict[str, float] = {}
        self.constants = {
            'pi': math.pi,
            'π': math.pi,
            'e': math.e,
            'phi': (1 + math.sqrt(5)) / 2,  # Золотое сечение
            'c': 299792458,  # Скорость света (м/с)
            'g': 9.80665,  # Ускорение свободного падения (м/с²)
        }
        self.history_file = os.path.expanduser('~/.calculator2025_history.json')
        self.load_history()

    def calculate(self, expression: str) -> float:
        """Вычисляет математическое выражение"""
        try:
            # Замена констант (только целые слова)
            expr = expression.lower()
            for const_name, const_value in self.constants.items():
                # Используем регулярное выражение с границами слов
                pattern = r'\b' + re.escape(const_name) + r'\b'
                expr = re.sub(pattern, str(const_value), expr)

            # Замена переменных (только целые слова)
            for var_name, var_value in self.variables.items():
                pattern = r'\b' + re.escape(var_name.lower()) + r'\b'
                expr = re.sub(pattern, str(var_value), expr)

            # Замена функций на их math эквиваленты
            expr = self._prepare_expression(expr)

            # Вычисление
            result = eval(expr, {"__builtins__": {}}, self._get_safe_dict())

            # Сохранение в историю
            self._add_to_history(expression, result)

            return result
        except Exception as e:
            raise ValueError(f"Ошибка вычисления: {str(e)}")

    def _prepare_expression(self, expr: str) -> str:
        """Подготавливает выражение для вычисления"""
        # Замены для удобного ввода
        replacements = {
            r'\^': '**',  # Степень
            r'√': 'sqrt',  # Квадратный корень
            r'×': '*',  # Умножение
            r'÷': '/',  # Деление
        }

        for pattern, replacement in replacements.items():
            expr = re.sub(pattern, replacement, expr)

        return expr

    def _get_safe_dict(self) -> Dict:
        """Возвращает безопасный словарь функций для eval"""
        return {
            # Базовые математические функции
            'abs': abs,
            'round': round,
            'min': min,
            'max': max,
            'sum': sum,

            # Модуль math
            'sqrt': math.sqrt,
            'pow': pow,
            'exp': math.exp,
            'log': math.log,
            'log10': math.log10,
            'log2': math.log2,

            # Тригонометрия
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'atan2': math.atan2,

            # Гиперболические функции
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,

            # Преобразования углов
            'degrees': math.degrees,
            'radians': math.radians,
            'deg': math.degrees,
            'rad': math.radians,

            # Другие функции
            'factorial': math.factorial,
            'gcd': math.gcd,
            'lcm': math.lcm,
            'floor': math.floor,
            'ceil': math.ceil,
            'trunc': math.trunc,
        }

    def _add_to_history(self, expression: str, result: float):
        """Добавляет вычисление в историю"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'expression': expression,
            'result': result
        }
        self.history.append(entry)
        self.save_history()

    def get_history(self, n: int = 10) -> List[Dict]:
        """Возвращает последние n записей истории"""
        return self.history[-n:]

    def clear_history(self):
        """Очищает историю"""
        self.history = []
        self.save_history()

    def save_history(self):
        """Сохраняет историю в файл"""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.history, f, indent=2)
        except Exception:
            pass  # Игнорируем ошибки сохранения

    def load_history(self):
        """Загружает историю из файла"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    self.history = json.load(f)
        except Exception:
            self.history = []

    # Функции памяти
    def memory_store(self, value: float):
        """Сохраняет значение в память"""
        self.memory = value

    def memory_recall(self) -> float:
        """Возвращает значение из памяти"""
        return self.memory

    def memory_clear(self):
        """Очищает память"""
        self.memory = 0.0

    def memory_add(self, value: float):
        """Добавляет значение к памяти"""
        self.memory += value

    def memory_subtract(self, value: float):
        """Вычитает значение из памяти"""
        self.memory -= value

    # Работа с переменными
    def set_variable(self, name: str, value: float):
        """Устанавливает переменную"""
        self.variables[name] = value

    def get_variable(self, name: str) -> Optional[float]:
        """Получает значение переменной"""
        return self.variables.get(name)

    def list_variables(self) -> Dict[str, float]:
        """Возвращает все переменные"""
        return self.variables.copy()

    def clear_variables(self):
        """Очищает все переменные"""
        self.variables = {}

    # Конвертация единиц
    def convert_units(self, value: float, from_unit: str, to_unit: str) -> float:
        """Конвертирует значение между единицами измерения"""
        conversions = {
            # Длина
            'mm_m': 0.001,
            'cm_m': 0.01,
            'km_m': 1000,
            'inch_m': 0.0254,
            'ft_m': 0.3048,
            'yard_m': 0.9144,
            'mile_m': 1609.34,

            # Масса
            'g_kg': 0.001,
            'mg_kg': 0.000001,
            'ton_kg': 1000,
            'lb_kg': 0.453592,
            'oz_kg': 0.0283495,

            # Температура (специальная обработка)
            'c_f': lambda c: c * 9/5 + 32,
            'f_c': lambda f: (f - 32) * 5/9,
            'c_k': lambda c: c + 273.15,
            'k_c': lambda k: k - 273.15,

            # Площадь
            'cm2_m2': 0.0001,
            'km2_m2': 1000000,
            'hectare_m2': 10000,

            # Объём
            'ml_l': 0.001,
            'cl_l': 0.01,
            'dl_l': 0.1,
            'gal_l': 3.78541,

            # Время
            'min_s': 60,
            'hour_s': 3600,
            'hour_min': 60,
            'day_s': 86400,
            'day_hour': 24,
            'week_s': 604800,
            'week_day': 7,
        }

        key = f"{from_unit}_{to_unit}"
        reverse_key = f"{to_unit}_{from_unit}"

        if key in conversions:
            factor = conversions[key]
            if callable(factor):
                return factor(value)
            return value * factor
        elif reverse_key in conversions:
            factor = conversions[reverse_key]
            if callable(factor):
                # Для температуры нужна обратная функция
                if reverse_key == 'c_f':
                    return (value - 32) * 5/9
                elif reverse_key == 'f_c':
                    return value * 9/5 + 32
                elif reverse_key == 'c_k':
                    return value - 273.15
                elif reverse_key == 'k_c':
                    return value + 273.15
            return value / factor
        else:
            raise ValueError(f"Неизвестная конвертация: {from_unit} -> {to_unit}")


class CalculatorCLI:
    """Интерфейс командной строки для калькулятора"""

    def __init__(self):
        self.calc = Calculator2025()
        self.running = True

    def print_banner(self):
        """Печатает баннер калькулятора"""
        print("\n" + "="*60)
        print("  ПРОДВИНУТЫЙ КАЛЬКУЛЯТОР 2025")
        print("  Научные функции | История | Конвертация единиц")
        print("="*60)
        print("\nВведите 'help' для справки, 'quit' для выхода\n")

    def print_help(self):
        """Печатает справку"""
        help_text = """
СПРАВКА ПО КАЛЬКУЛЯТОРУ 2025

БАЗОВЫЕ ОПЕРАЦИИ:
  + - * /           Сложение, вычитание, умножение, деление
  ** или ^          Возведение в степень
  sqrt(x)           Квадратный корень
  abs(x)            Абсолютное значение

НАУЧНЫЕ ФУНКЦИИ:
  sin(x), cos(x), tan(x)      Тригонометрические функции (радианы)
  asin(x), acos(x), atan(x)   Обратные тригонометрические
  log(x), log10(x), log2(x)   Логарифмы
  exp(x)                      Экспонента
  factorial(n)                Факториал

КОНСТАНТЫ:
  pi, π             Число Пи (3.14159...)
  e                 Число Эйлера (2.71828...)
  phi               Золотое сечение (1.61803...)
  c                 Скорость света (м/с)
  g                 Ускорение свободного падения

РАБОТА С ПАМЯТЬЮ:
  mem store <значение>     Сохранить в память
  mem recall              Вспомнить из памяти
  mem clear               Очистить память
  mem add <значение>      Добавить к памяти
  mem sub <значение>      Вычесть из памяти

ПЕРЕМЕННЫЕ:
  var set <имя> <значение>    Установить переменную
  var get <имя>               Получить значение
  var list                    Показать все переменные
  var clear                   Очистить все переменные

КОНВЕРТАЦИЯ ЕДИНИЦ:
  convert <значение> <из> <в>
  Примеры: convert 100 cm m
           convert 32 f c
           convert 5 km mile

ИСТОРИЯ:
  history              Показать последние 10 вычислений
  history <n>          Показать последние n вычислений
  clear history        Очистить историю

КОМАНДЫ:
  help                 Показать эту справку
  quit, exit           Выход из калькулятора

ПРИМЕРЫ:
  2 + 2 * 3
  sqrt(144)
  sin(pi/2)
  log(e**2)
  convert 100 cm m
"""
        print(help_text)

    def run(self):
        """Запускает интерактивный режим"""
        self.print_banner()

        while self.running:
            try:
                user_input = input(">>> ").strip()

                if not user_input:
                    continue

                # Обработка команд
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\nДо свидания!")
                    break

                elif user_input.lower() == 'help':
                    self.print_help()

                elif user_input.lower().startswith('history'):
                    self._handle_history(user_input)

                elif user_input.lower().startswith('clear history'):
                    self.calc.clear_history()
                    print("История очищена")

                elif user_input.lower().startswith('mem '):
                    self._handle_memory(user_input)

                elif user_input.lower().startswith('var '):
                    self._handle_variables(user_input)

                elif user_input.lower().startswith('convert '):
                    self._handle_conversion(user_input)

                else:
                    # Вычисление выражения
                    result = self.calc.calculate(user_input)
                    print(f"\n  = {result}\n")

            except KeyboardInterrupt:
                print("\n\nДо свидания!")
                break
            except Exception as e:
                print(f"\nОшибка: {str(e)}\n")

    def _handle_history(self, command: str):
        """Обрабатывает команды истории"""
        parts = command.split()
        n = 10
        if len(parts) > 1 and parts[1].isdigit():
            n = int(parts[1])

        history = self.calc.get_history(n)
        if not history:
            print("История пуста")
            return

        print("\nИСТОРИЯ ВЫЧИСЛЕНИЙ:")
        print("-" * 60)
        for i, entry in enumerate(history, 1):
            timestamp = entry['timestamp'][:19]  # Убираем микросекунды
            expr = entry['expression']
            result = entry['result']
            print(f"{i}. [{timestamp}]")
            print(f"   {expr} = {result}")
        print()

    def _handle_memory(self, command: str):
        """Обрабатывает команды памяти"""
        parts = command.split()

        if len(parts) < 2:
            print("Неверная команда памяти")
            return

        action = parts[1].lower()

        if action == 'store' and len(parts) > 2:
            value = float(parts[2])
            self.calc.memory_store(value)
            print(f"Сохранено в память: {value}")

        elif action == 'recall':
            value = self.calc.memory_recall()
            print(f"Значение из памяти: {value}")

        elif action == 'clear':
            self.calc.memory_clear()
            print("Память очищена")

        elif action == 'add' and len(parts) > 2:
            value = float(parts[2])
            self.calc.memory_add(value)
            print(f"Добавлено к памяти: {value}, новое значение: {self.calc.memory}")

        elif action == 'sub' and len(parts) > 2:
            value = float(parts[2])
            self.calc.memory_subtract(value)
            print(f"Вычтено из памяти: {value}, новое значение: {self.calc.memory}")

        else:
            print("Неверная команда памяти")

    def _handle_variables(self, command: str):
        """Обрабатывает команды переменных"""
        parts = command.split()

        if len(parts) < 2:
            print("Неверная команда переменных")
            return

        action = parts[1].lower()

        if action == 'set' and len(parts) > 3:
            name = parts[2]
            value = float(parts[3])
            self.calc.set_variable(name, value)
            print(f"Переменная {name} = {value}")

        elif action == 'get' and len(parts) > 2:
            name = parts[2]
            value = self.calc.get_variable(name)
            if value is not None:
                print(f"{name} = {value}")
            else:
                print(f"Переменная {name} не найдена")

        elif action == 'list':
            variables = self.calc.list_variables()
            if variables:
                print("\nПЕРЕМЕННЫЕ:")
                for name, value in variables.items():
                    print(f"  {name} = {value}")
                print()
            else:
                print("Переменные не заданы")

        elif action == 'clear':
            self.calc.clear_variables()
            print("Все переменные очищены")

        else:
            print("Неверная команда переменных")

    def _handle_conversion(self, command: str):
        """Обрабатывает конвертацию единиц"""
        parts = command.split()

        if len(parts) < 4:
            print("Использование: convert <значение> <из> <в>")
            return

        try:
            value = float(parts[1])
            from_unit = parts[2].lower()
            to_unit = parts[3].lower()

            result = self.calc.convert_units(value, from_unit, to_unit)
            print(f"\n  {value} {from_unit} = {result} {to_unit}\n")
        except Exception as e:
            print(f"Ошибка конвертации: {str(e)}")


def main():
    """Главная функция"""
    cli = CalculatorCLI()
    cli.run()


if __name__ == '__main__':
    main()
