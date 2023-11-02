def change_date_format(date: str) -> str:
    """Change date format from dd/mm/yyyy to yyyy-mm-dd

    Args:
        date (str): date in dd/mm/yyyy format

    Returns:
        str: date in yyyy-mm-dd format
    """
    date = date.split("/")
    return f"{date[2]}-{date[1]}-{date[0]}"