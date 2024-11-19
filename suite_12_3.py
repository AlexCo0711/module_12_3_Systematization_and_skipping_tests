# Домашнее задание по теме "Систематизация и пропуск тестов".
# TestSuit
# импорт необходимых библиотек и файлов
import unittest
import module_12_1
import module_12_2


# объявление переменной suite_test объекта TestSuite модуля unittest
suite_test = unittest.TestSuite()
# Добавляю тесты RunnerTest и TournamentTest в этот TestSuit.
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

# Создание объекта класса TextTestRunner, с аргументом verbosity=2.
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite_test)