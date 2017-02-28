import fileinput
import re

from tempfile import mkstemp
from shutil import move
from os import remove, close

file_path = "/Users/Marcell_Pataky/Desktop/parser/ExpenseReportCtcService.java"

deprecated_logger_import = "import com.epam.ctc.core.logger.Logger;"

loggerfactory_import = "import org.slf4j.LoggerFactory;\nimport org.slf4j.Logger;"

logger_instantiation = "private static final Logger LOGGER = LoggerFactory.getLogger(BusinessTripCtcService.class);"

get_class_and_method_names = "Logger.getClassAndMethodNames()"


def replace(pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


def rename_logger_call(text_to_be_renamed):
    return text_to_be_renamed.replace("Logger", "LOGGER")


def remove_getClassAndMethodNames_call(text_to_be_replaced):
    return re.sub("Logger.getClassAndMethodNames\(\)\s*\+\s*", "", text_to_be_replaced)


def replace_logger_line(text):
    text = remove_getClassAndMethodNames_call(text)
    text = rename_logger_call(text)
    return text


with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(deprecated_logger_import, loggerfactory_import), end='')
        if line.lstrip().startswith("Logger."):
            old_line = line
            new_line = replace_logger_line(line)
            print(line.replace(old_line, new_line), end='')

file.close()
