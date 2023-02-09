import datetime

def logger(path):
    def _logger(old_function):
        def new_function(*args,**kwargs):
            result = old_function(*args, **kwargs)
            log_content = f'Дата и время вызова функции - {datetime.datetime.now()}\n '\
                          f'Имя  функции - {old_function.__name__}\n'\
                          f'Аргументы функции - {args},{kwargs}\n'\
                          f'Возвращаемое значение - {result}'
            with open(path,'w') as log_file:
                log_file.writelines(log_content)
            return result
        return new_function
    return _logger
