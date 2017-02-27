import fileinput
import re

file_path = "/Users/Marcell_Pataky/Desktop/parser/ExpenseReportCtcService.java"

deprecated_logger_import = "import com.epam.ctc.core.logger.Logger;"

loggerfactory_import = "import org.slf4j.LoggerFactory;\nimport org.slf4j.Logger;"

logger_instantiation = "private static final Logger LOGGER = LoggerFactory.getLogger(BusinessTripCtcService.class);"

get_class_and_method_names = "Logger.getClassAndMethodNames()"


def rename_logger_call(logger):
    return logger.replace("Logger", "LOGGER")


def remove_getClassAndMethodNames_call(method_call):
    return re.sub("Logger.getClassAndMethodNames\(\)\s*\+\s*", "", method_call)


def replace_logger_line(text):
    if text.lstrip().startswith("Logger."):
        text = remove_getClassAndMethodNames_call(text)
        text = rename_logger_call(text)
        return text


file = open(file_path, "r")

for line in file:
    if line.lstrip().startswith("Logger."):
        print(replace_logger_line(line))

file.close()
