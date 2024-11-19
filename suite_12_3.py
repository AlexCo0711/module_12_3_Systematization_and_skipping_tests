# Домашнее задание по теме "Систематизация и пропуск тестов".
# TestSuit
# импорт необходимых библиотек и файлов
import unittest
import test_12_3

# объявление переменной suite_test объекта TestSuite модуля unittest
suite_test = unittest.TestSuite()
# Добавляю тесты RunnerTest и TournamentTest в этот TestSuit.
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

# Создание объекта класса TextTestRunner, с аргументом verbosity=2.
runner = unittest.TextTestRunner(verbosity=2)
# запуск объекта runner
runner.run(suite_test)
