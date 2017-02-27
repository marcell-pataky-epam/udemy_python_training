import fileinput
import re

file_path = "/Users/Marcell_Pataky/Desktop/parser/ExpenseReportCtcService.java"

deprecated_logger_import = "import com.epam.ctc.core.logger.Logger;"

loggerfactory_import = "import org.slf4j.LoggerFactory;\nimport org.slf4j.Logger;"

logger_instantiation = "private static final Logger LOGGER = LoggerFactory.getLogger(BusinessTripCtcService.class);"

get_class_and_method_names = "Logger.getClassAndMethodNames()"


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
            print(line.replace(line, replace_logger_line(line)), end='')

file.close()
