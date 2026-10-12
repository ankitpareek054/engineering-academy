def extract_server_errors(requests):
    server_errors_requests = []
    for request in requests:
        if request['status'] >= 500 and request['status'] < 600:

            server_errors_requests.append({'request_id': request['request_id'], 'duration_seconds':request['duration_ms']/1000})
        
    return server_errors_requests

if __name__ =='__main__':

    assert extract_server_errors([]) == []

    assert extract_server_errors([
     {"request_id": "a", "status": 499, "duration_ms": 100},
        {"request_id": "b", "status": 500, "duration_ms": 200},
        {"request_id": "c", "status": 599, "duration_ms": 300},
        {"request_id": "d", "status": 600, "duration_ms": 400}
    ]) == [
        {"request_id": "b", "duration_seconds": 0.2},
        {"request_id": "c", "duration_seconds": 0.3}
    ]