def check_data_type(data):
    """
    判断数据是字符串类型还是列表类型。

    参数:
        data: 待检查的数据。

    返回:
        str: 如果数据类型是字符串。
        list: 如果数据类型是列表。
        None: 如果数据类型既不是字符串也不是列表。
    """
    if type(data) is str:
        return "str"
    elif type(data) is list:
        return "list"
    else:
        return None

