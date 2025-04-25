from botasaurus.request import request, Request
from botasaurus_requests.response import Response

@request(output=None, create_error_logs=False)
def botasaurus_get(req: Request, url: str, headers: dict = None) -> Response:
    """ General purpose "get" function that uses Botasaurus.
    
    Parameters
    ----------
    req : botasaurus.request.Request
        The request object provided by the botasaurus decorator
    url : str
        The URL to request
    headers : dict, optional
        Headers to include in the request
        
    Returns
    -------
    botasaurus_requests.response.Response
        The response from the request
    """
    if not isinstance(url, str):
        raise TypeError('`url` must be a string.')

    if headers is not None and not isinstance(headers, dict):
        raise TypeError('`headers` must be a dictionary or None.')

    resp = req.get(url, headers=headers)
    return resp
