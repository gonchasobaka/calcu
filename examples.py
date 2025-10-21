#!/usr/bin/env python3
"""
Примеры использования калькулятора 2025
Демонстрирует различные возможности калькулятора
"""

from calculator2025 import Calculator2025


def run_examples():
    """Запускает примеры использования калькулятора"""

    calc = Calculator2025()

    print("="*70)
    print("  ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ КАЛЬКУЛЯТОРА 2025")
    print("="*70)

    # Базовые операции
    print("\n1. БАЗОВЫЕ ОПЕРАЦИИ")
    print("-" * 70)
    examples = [
        "2 + 2",
        "10 - 3",
        "5 * 6",
        "100 / 4",
        "2 ** 8",
        "(10 + 5) * 3",
    ]

    for expr in examples:
        result = calc.calculate(expr)
        print(f"  {expr:<20} = {result}")

    # Научные функции
    print("\n2. НАУЧНЫЕ ФУНКЦИИ")
    print("-" * 70)
    examples = [
        "sqrt(144)",
        "sqrt(2)",
        "pow(2, 10)",
        "abs(-42)",
        "factorial(5)",
        "log(e)",
        "log10(1000)",
        "exp(1)",
    ]

    for expr in examples:
        result = calc.calculate(expr)
        print(f"  {expr:<20} = {result}")

    # Тригонометрия
    print("\n3. ТРИГОНОМЕТРИЯ")
    print("-" * 70)
    examples = [
        "sin(0)",
        "sin(pi/2)",
        "cos(0)",
        "cos(pi)",
        "tan(pi/4)",
        "asin(1)",
        "radians(180)",
        "degrees(pi)",
    ]

    for expr in examples:
        result = calc.calculate(expr)
        print(f"  {expr:<20} = {result}")

    # Использование констант
    print("\n4. КОНСТАНТЫ")
    print("-" * 70)
    examples = [
        "pi",
        "e",
        "phi",
        "2 * pi",
        "e ** 2",
        "sqrt(5) / 2 + 0.5",  # Должно равняться phi
    ]

    for expr in examples:
        result = calc.calculate(expr)
        print(f"  {expr:<20} = {result}")

    # Работа с переменными
    print("\n5. ПЕРЕМЕННЫЕ")
    print("-" * 70)
    calc.set_variable('x', 10)
    calc.set_variable('y', 20)
    calc.set_variable('radius', 5)

    print("  Установлены переменные: x=10, y=20, radius=5")
    print()

    examples = [
        "x + y",
        "x * y",
        "2 * pi * radius",  # Длина окружности
        "pi * radius ** 2",  # Площадь круга
    ]

    for expr in examples:
        result = calc.calculate(expr)
        print(f"  {expr:<25} = {result}")

    # Память
    print("\n6. РАБОТА С ПАМЯТЬЮ")
    print("-" * 70)
    calc.memory_store(100)
    print(f"  Сохранено в память: 100")
    print(f"  Память: {calc.memory_recall()}")

    calc.memory_add(50)
    print(f"  Добавлено 50")
    print(f"  Память: {calc.memory_recall()}")

    calc.memory_subtract(30)
    print(f"  Вычтено 30")
    print(f"  Память: {calc.memory_recall()}")

    # Конвертация единиц
    print("\n7. КОНВЕРТАЦИЯ ЕДИНИЦ")
    print("-" * 70)
    conversions = [
        (100, 'cm', 'm'),
        (1, 'km', 'm'),
        (1, 'm', 'ft'),
        (32, 'f', 'c'),
        (0, 'c', 'f'),
        (100, 'c', 'k'),
        (1, 'kg', 'lb'),
        (1, 'l', 'ml'),
        (1, 'hour', 's'),
        (1, 'day', 'hour'),
    ]

    for value, from_unit, to_unit in conversions:
        result = calc.convert_units(value, from_unit, to_unit)
        print(f"  {value} {from_unit:<6} = {result:>12.4f} {to_unit}")

    # Сложные вычисления
    print("\n8. СЛОЖНЫЕ ВЫЧИСЛЕНИЯ")
    print("-" * 70)
    examples = [
        "sqrt(pow(3, 2) + pow(4, 2))",  # Гипотенуза треугольника 3-4-5
        "log10(10 ** 3)",
        "sin(pi/6) ** 2 + cos(pi/6) ** 2",  # Должно быть 1
        "factorial(10) / factorial(8)",
        "gcd(48, 18)",
        "lcm(12, 18)",
    ]

    for expr in examples:
        result = calc.calculate(expr)
        print(f"  {expr:<45} = {result}")

    # Физические формулы
    print("\n9. ФИЗИЧЕСКИЕ ФОРМУЛЫ")
    print("-" * 70)

    # Кинетическая энергия: E = (m * v^2) / 2
    m = 10  # масса в кг
    v = 20  # скорость в м/с
    calc.set_variable('m', m)
    calc.set_variable('v', v)
    kinetic_energy = calc.calculate('(m * v ** 2) / 2')
    print(f"  Кинетическая энергия (m={m}кг, v={v}м/с): {kinetic_energy} Дж")

    # Потенциальная энергия: E = m * g * h
    h = 10  # высота в метрах
    calc.set_variable('h', h)
    potential_energy = calc.calculate('m * g * h')
    print(f"  Потенциальная энергия (m={m}кг, h={h}м): {potential_energy} Дж")

    # Период колебаний маятника: T = 2 * pi * sqrt(L / g)
    L = 1  # длина в метрах
    calc.set_variable('L', L)
    period = calc.calculate('2 * pi * sqrt(L / g)')
    print(f"  Период колебаний маятника (L={L}м): {period:.4f} с")

    # Длина волны де Бройля: λ = h / (m * v)
    h_planck = 6.62607015e-34  # постоянная Планка
    m_electron = 9.10938356e-31  # масса электрона
    v_electron = 1e6  # скорость электрона
    calc.set_variable('h_planck', h_planck)
    calc.set_variable('m_electron', m_electron)
    calc.set_variable('v_electron', v_electron)
    wavelength = calc.calculate('h_planck / (m_electron * v_electron)')
    print(f"  Длина волны де Бройля: {wavelength:.4e} м")

    # История
    print("\n10. ИСТОРИЯ ВЫЧИСЛЕНИЙ")
    print("-" * 70)
    history = calc.get_history(5)
    print(f"  Всего вычислений в истории: {len(calc.history)}")
    print(f"  Последние 5 записей:")
    for i, entry in enumerate(history, 1):
        print(f"    {i}. {entry['expression']:<30} = {entry['result']}")

    print("\n" + "="*70)
    print("  ПРИМЕРЫ ЗАВЕРШЕНЫ")
    print("="*70)


def test_calculator():
    """Простые тесты калькулятора"""

    calc = Calculator2025()

    print("\n" + "="*70)
    print("  ТЕСТЫ КАЛЬКУЛЯТОРА")
    print("="*70 + "\n")

    tests = [
        ("2 + 2", 4.0),
        ("10 - 3", 7.0),
        ("5 * 6", 30.0),
        ("100 / 4", 25.0),
        ("2 ** 10", 1024.0),
        ("sqrt(144)", 12.0),
        ("abs(-42)", 42.0),
        ("sin(0)", 0.0),
        ("cos(0)", 1.0),
        ("log10(1000)", 3.0),
        ("factorial(5)", 120.0),
    ]

    passed = 0
    failed = 0

    for expr, expected in tests:
        try:
            result = calc.calculate(expr)
            if abs(result - expected) < 1e-10:  # Учитываем погрешность вычислений
                print(f"✓ {expr:<20} = {result} (OK)")
                passed += 1
            else:
                print(f"✗ {expr:<20} = {result}, ожидалось {expected} (FAIL)")
                failed += 1
        except Exception as e:
            print(f"✗ {expr:<20} - Ошибка: {e} (FAIL)")
            failed += 1

    print(f"\nРезультаты: {passed} успешно, {failed} неудачно")
    print("="*70 + "\n")


if __name__ == '__main__':
    run_examples()
    test_calculator()
