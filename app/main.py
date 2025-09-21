def format_linter_error(error: dict) -> dict:
    """
       Formatting single error to correct format

       :param error: dict with error
       :return: formatted dict with correct keys
       """
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """
    Formatting list with errors and file
    path where it was to a dict

    :param
        file_path: string with file path where was error
        errors: list with unformatted errors
    :return: formatted dict with correct keys and path
    """
    return {"errors":
            [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "failed" if errors else "passed"
            }


def format_linter_report(linter_report: dict) -> list:
    """
        Formattind dictionary report to correct format

        :param linter_report: unformatted linter report
        :return: formatted list with dictionaries of reports
        """
    return [format_single_linter_file(path, errors)
            for path, errors in linter_report.items()]
