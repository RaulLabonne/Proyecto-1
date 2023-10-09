
def writeError():
    """ Gives a message for a write error.

    Returns
    -------
    str
        The message that will show in 404.html.
    """

    return "lo la ciudad que buscas o ticket no estan en la base de datos"


def readError():
    """ Gives a message for a read error.

    Returns
    -------
    str
        The message that will show in 404.html.
    """

    return "la base de datos no esta o contiene datos erroneos"


def apiError(num):
    """ Gives a message for an API error.

    If the number is 1, then the apy key is wrong write, in other case the error is of the server.

    Parameters
    ----------
    num : int, optional
        Type of error that happened

    Returns
    -------
    str
        The message that will show in 404.html
    """

    if (num == 1):
        return "tu API key no es valida, revisala"
    return "la API no responde, intente mas tarde"


def errorCall():
    """ Gives a message for a call error, this only occurs if the limit of API calls is exceeded

    Returns
    -------
    str
        The message that will show in 404.html.
    """
    return "se han superado el limite de llamadas permitidas, por favor espere un minuto o se baneara su API"